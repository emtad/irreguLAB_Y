---
Date: 2026-05-22
---

# Context

## Starting point

## Goals

# Setup

## Considerations

Due to time constraints we developed and tested our workflow on a single demonstrator object. To make a meaningful performance evaluation a large volume of repeated tests in which in addition to material instances, the assembly topology is varied would be required.

As the input material is by its nature irregular and unique, tests can never be repeated with the same parameter and therefore an analogous comparison to a baseline can only be simulated.

The main metric of fabrication performance is quantified as simulated machining time. Elapsed machining time is not measured as well as time required for setup, programming and troubleshooting is omitted as both are assumed to be non-representative due to excess incontrollable variables (operator practice and learning process, machining interrupts, varied machining speed to test material behaviour). Exemplarily, we can compare the elapsed machining time of a fork and its simulated time.

In addition to simulated machining time, other performance metrics could be quantified:

-   resulting surface quality
-   surface defect occurrence (area)
-   target geometry deviation

## Parameters

We have two main variable spaces - the employed milling technique and the designed target geometry.

-   geometry

    -   ruled-surface geometry → to test
    -   SubD base geometry → baseline
    -   fork scans → constant
    -   fixation geometry → constant (optimized for ruled-surface geometry, but kept constant for comparability)

-   milling

    -   5-axis flank milling → to test
    -   layer-based milling → baseline
    -   tool-flute → constant
    -   speed → constant (during fabrication heavily manually varied, but kept constant in simulation for comparability)

-   goals
    -   surface quality → constant

## Data Collection

-   simulated machining time (differentiated into roughing and finishing)

    -   5-axis flank milling - ruled-surface geometry → test
    -   layer-based milling - ruled-surface geometry → baseline milling technique
    -   layer-based milling - SubD base geometry → baseline geometry

-   geometry properties → normalize machining time against milled area

    -   ruled-surface geometry surface area
    -   SubD base geometry surface

## Method

-   Simulation in CAM Software (TEBIS) under fabrication parameters

## Evaluation Metrics

-   total (roughing, finishing and combined) machining time
-   average machining time (combined) → percentage difference of test against both baselines
-   average quotient of machining time (combined) per fork geometry surface area

# Hypothesis

# Data

# Results
