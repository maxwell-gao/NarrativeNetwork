# NarrativeSphereAI

This project is a narrative experiment that simulates an ecosystem using a directed graph structure. Agents (nodes) interact with each other by exchanging information, forming connections, and manipulating the graph structure. The project uses Python and the `networkx` library to represent the graph and simulate agent behavior.

## Overview

The project simulates an ecosystem where agents (nodes) interact within a directed graph. Agents can:

- Form connections (edges) with other agents.
- Disconnect from other agents.
- Reverse the direction of connections.
- Exchange information and update their internal state.

The graph structure is represented using the `networkx` library, and the system supports serialization of the graph to JSON for easy storage and analysis.

