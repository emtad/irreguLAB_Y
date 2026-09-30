import os
import json
import tempfile
import shutil

import Rhino


class FileManager(object):
    """
    JSON / JSONL file manager for Grasshopper.
    """

    SUPPORTED_FORMATS = ("json", "jsonl")

    def __init__(self, f="json", name="file", path=None):
        self.f = str(f).lower().lstrip(".")

        if self.f not in self.SUPPORTED_FORMATS:
            raise ValueError(
                "Unsupported file format '{}'. "
                "Supported formats: {}".format(
                    self.f, ", ".join(self.SUPPORTED_FORMATS)
                )
            )

        self.path = self._resolve_path(path, name)

    # ------------------------------------------------------------------
    # PATH HANDLING
    # ------------------------------------------------------------------

    def _resolve_path(self, path, name):
        """
        Resolve the target path.

        If an explicit path is supplied, use it.
        Otherwise construct a path next to the active Rhino document.
        """

        if path is not None:
            path = os.path.abspath(os.path.expanduser(str(path)))

            directory = os.path.dirname(path)

            if not directory:
                raise ValueError(
                    "The supplied path does not contain a valid directory:\n{}".format(
                        path
                    )
                )

            if not os.path.isdir(directory):
                raise IOError(
                    "Directory does not exist:\n{}".format(directory)
                )

            # Remove existing extension and apply requested format.
            base, _ = os.path.splitext(path)

            return base + "." + self.f

        # No path supplied -> use active Rhino document.
        doc = Rhino.RhinoDoc.ActiveDoc

        if doc is None:
            raise RuntimeError(
                "No active Rhino document. "
                "Save the Rhino file or provide an explicit file path."
            )

        doc_path = doc.Path

        if not doc_path:
            raise RuntimeError(
                "The Rhino document has not been saved. "
                "Save the Rhino file or provide an explicit file path."
            )

        directory = os.path.dirname(doc_path)
        filename = os.path.splitext(os.path.basename(doc_path))[0]

        if not name:
            name = "file"

        filename = "{}_{}".format(name, filename)

        return os.path.join(
            directory,
            filename + "." + self.f
        )

    # ------------------------------------------------------------------
    # WRITE
    # ------------------------------------------------------------------

    def write(self, data):
        """
        Write JSON/JSONL data safely.

        JSON uses an atomic temporary-file replacement so an interrupted
        write is less likely to corrupt the existing file.
        """

        directory = os.path.dirname(self.path)

        if not os.path.isdir(directory):
            raise IOError(
                "Target directory does not exist:\n{}".format(directory)
            )

        if self.f == "json":
            self._write_json(data)

        elif self.f == "jsonl":
            self._write_jsonl(data)

        return self

    def _write_json(self, data):
        """
        Atomically replace the existing JSON file.
        """

        fd, temp_path = tempfile.mkstemp(
            prefix=".__tmp_",
            suffix=".json",
            dir=os.path.dirname(self.path)
        )

        try:
            with os.fdopen(fd, "w") as f:
                json.dump(
                    data,
                    f,
                    indent=2,
                    ensure_ascii=False
                )

                # Make sure data is physically flushed as far as
                # Python can reasonably guarantee.
                f.flush()
                os.fsync(f.fileno())

            # Atomic replacement where supported.
            if os.path.exists(self.path):
                os.replace(temp_path, self.path)
            else:
                os.rename(temp_path, self.path)

        except Exception:
            if os.path.exists(temp_path):
                try:
                    os.remove(temp_path)
                except Exception:
                    pass

            raise

    def _write_jsonl(self, data):
        """
        Append one JSON object/value per line.
        """

        try:
            with open(self.path, "a") as f:
                f.write(
                    json.dumps(
                        data,
                        ensure_ascii=False
                    )
                    + "\n"
                )

        except TypeError as e:
            raise TypeError(
                "Data could not be serialized to JSONL: {}".format(e)
            )

    # ------------------------------------------------------------------
    # READ
    # ------------------------------------------------------------------

    def read(self):
        """
        Read JSON/JSONL.

        Raises useful exceptions rather than terminating the
        Grasshopper process.
        """

        if not os.path.isfile(self.path):
            raise IOError(
                "File not found:\n{}".format(self.path)
            )

        if not os.access(self.path, os.R_OK):
            raise IOError(
                "File is not readable:\n{}".format(self.path)
            )

        if self.f == "json":
            return self._read_json()

        elif self.f == "jsonl":
            return self._read_jsonl()

        raise ValueError(
            "Unsupported file format: {}".format(self.f)
        )

    def _read_json(self):
        try:
            with open(self.path, "r") as f:
                return json.load(f)

        except ValueError as e:
            raise ValueError(
                "Invalid JSON in file:\n{}\n\n{}".format(
                    self.path,
                    e
                )
            )

        except OSError as e:
            raise IOError(
                "Could not read file:\n{}\n\n{}".format(
                    self.path,
                    e
                )
            )

    def _read_jsonl(self):
        content = []

        try:
            with open(self.path, "r") as f:

                for line_number, line in enumerate(f, 1):

                    line = line.strip()

                    # Ignore empty lines.
                    if not line:
                        continue

                    try:
                        content.append(json.loads(line))

                    except ValueError as e:
                        raise ValueError(
                            "Invalid JSON on line {} "
                            "in file:\n{}\n\n{}".format(
                                line_number,
                                self.path,
                                e
                            )
                        )

        except OSError as e:
            raise IOError(
                "Could not read file:\n{}\n\n{}".format(
                    self.path,
                    e
                )
            )

        return content

    # ------------------------------------------------------------------
    # RESET
    # ------------------------------------------------------------------

    def reset(self):
        """
        Rename the current file to a backup.

        Creates a unique backup filename rather than overwriting
        an existing backup.
        """

        if not os.path.isfile(self.path):
            raise IOError(
                "File not found:\n{}".format(self.path)
            )

        backup_path = self.path + ".bak"

        counter = 1

        while os.path.exists(backup_path):
            backup_path = "{}.{}.bak".format(
                self.path,
                counter
            )
            counter += 1

        try:
            os.rename(self.path, backup_path)

        except OSError as e:
            raise IOError(
                "Could not create backup:\n{}\n\n{}".format(
                    self.path,
                    e
                )
            )

        return self