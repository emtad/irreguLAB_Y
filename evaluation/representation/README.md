---
Date: 2026-05-22
---

# Context

## Starting point

- exploring alternate types of fork **representation** to scan-based approaches suitable for in-situ design
- exploring different approaches to inventory management
## Goals

- representation
	- fast, in-situ capture in continuous interface
	- sufficient performance in MR-interface → minimum viable vertice/polygon count
	- good-enough-geometry for containment testing → visual coherence over accuracy (accuracy/deviation from actual geometry not that important, as long as its contained)

- usage
	- extracting and processing a minimum amount of forks → high usage to extraction ratio

# Setup
## Considerations

- what are parameters and is available data of comparable projects?

	- *Conceptual Joining: Wood Structures from Detail to Utopia*
		-  "The first realized demonstrator from 59 branches at the Conceptual Joining show at the Angewandte Innovation Laboratory (AIL) (Fig. 18) was a cutout from a larger aggregation model made of 788 elements designed for a load case scenario that assumed an architectural scheme with platforms and ramps (Fig. 16g, p. 147 and Fig. 19)."
		- visualization shows 85 forks clustered into 8 proto-parts
		→ non representative/comparable because their approach is to aggregate all forks
	
	- Wild Wood Grishells
		- "After sorting out forks that were too irregular or whose diameters were too small (<2”), the research inventory comprised 44 tree forks that were then 3D scanned using photogrammetry with smartphone camera pictures with Metashape and characterized to constitute a digital inventory (Figure 13)."
		- "The selected design iteration has a topology with 38 nodes, and the inventory only contained 44 elements; this was a constrained inventory design problem with 86% of the elements used."
		  → very efficient
		  
	- LIMB
		- "The team acquired 72 tree crotches from different wood yards near Ann Arbor."
		- "All of the pieces were milled and sealed using a sealant to delay drying and cracking. The end of each limb of the crotch was milled to accommodate a peg connection to the linear connection member. Milled pieces were stored for assembly. Figure 14 shows a piece mounted in the milling jig at the conclusion of the 3D routing operation. Every piece went through this process which took about 2 hours each."
	
	- Wood Chip Barn
		- "The building’s primary structure is an arching truss consisting of 20 discrete beech forks[...]"
		- "First, a photographic survey of 204 standing beech trees provided approximate two-dimensional fork representations with enough detail to make informed decisions on which trees to cut down. Following the harvesting of 25 selected trees, a second more detailed 3D-scan of each fork was carried out which allowed for the development of the final truss configuration from these forks’ specific geometric forms."
		- "From this analysis a shortlist of 40 forks to be considered for felling was generated [...]"
		- "of these, 25 beech forks were successfully harvested. Once transported back to the yard, a detailed photogrammetric 3D-scan was made of each in order to capture their complex forms. "
		- "Of these, 25 beech forks were successfully harvested."
		- note: count for "forks" and "trees" used interchangeably - probably as only one fork per tree (first bifurcation) is considered

	- Timber De-standardized 1.0
		- The structure uses a total of 16 salvaged tree logs cut into 18 members (Figure 15) with 28 dowel connections."

	- Integrated workflow for cooperative robotic fabrication of natural tree fork structures
		- "A collection of **91 wood components**, comprising **30 curved components and 61 forked components** (Fig. 18), was randomly gathered from the harvesting site.”

| project                    | sighted              | sourced        | scanned         | processed | used |
| -------------------------- | -------------------- | -------------- | --------------- | --------- | ---- |
| Wild Wood Gridshells       | -                    | 44             | 44              | -         | 38   |
| LIMB                       | -                    | 72             | 72              | -         | -    |
| Wood Chip Barn             | 204 (40 shortlisted) | 31 (25 usable) | 25              | 20        | 20   |
| Timber De-standardized 1.0 | -                    | -              | - (at least 16) | -         | 16   |
| Integrated workflow        | 91 (61 forks)        | 61             | 61              | -         |      |
	→ lack of unified/comparable data


- what are parameters and is data we have or can measure?

	- fork count
		- captured
			- traced
			- hi-res scanned
		- selected
		- sourced
		- processed
		→ n_scanned = n_selected = n_sourced = n_processed

	- fork representation metrics
		- vertice count per surface area
			- fork-tracing
			- raw scan
			- reduced scan
		- file size
			- Rhino file size
			- JSON file size


- possible performance metrics

	- comparison of file size of fork representation types (scan vs tracing) extrapolated to inventory instance count (similar project average sourced fork count per used fork count vs gleaning-table traced count vs sourced/selected count)
		- "compared to other projects with an average fork contenders per selected forks → x times 8 forks as scans vs. 20 fork sketches vs x times 8 fork sketches"
		- "if as in other projects all 20 possible fork-contenders (already visually pre-sorted) were scanned, an additional amount of "

##  Parameters

### Constants

- inventory
- representation types

### Variables

- raw scan
	- surface area
	- vertice count
	- polygon count
	- file size (STL)

- processed scan
	- deviation from raw scan → set to max. 5mm RMSE
	- surface area
	- vertice count
	- polygon count

- fork tracing
	- deviation from raw scan
	- surface area
	- vertice count
	- polygon count

## Baseline

-
## Method

- Rhino for pre-alignment of scans
- Meshlab for deviation analysis

## Evaluation Metrics

- comparison raw scan - processed scan - fork tracing
	- average file size in KB
	- average $\frac{n_{verticeCount}}{A_{surfaceArea}}$ in 1/dm²
	- average deviation RMSE in mm

- average tracing time

# Hypothesis

# Data

# Results


