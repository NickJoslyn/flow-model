# flow-model
Repository for location analysis with path-based demands

Location Analysis (LA) is a subset of operations research. Specifically, LA seeks to optimize the placement of facilities to satisfy some set of demands. 

Often, demands can be represented as points with a weight allocation. The total set of demands then looks like a simple network. Such a network can be optimized by p-median, maximal covering, and other models. The models are NP-Hard and require heuristic algorithms to solve reasonably sized demand networks. See location-analysis-Python and location-analysis-R for such methods.

The representation of a demand at a certain location is not applicable in all scenarios. For instance, think of traffic as your demand. Traffic follows a path -- a road -- and approximating as one location is unrealistic. As such, flow-based LA models manifested in the literature. Although flow-based models are largely utilized for alternative fuel station location, billboards, and impulse items (fast food), we seek an implementation to mathematically support our decisions to improve water quality.
