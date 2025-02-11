

```Plain Text
 |\ |  _. ._ ._ _. _|_ o     _  |\ |  _ _|_       _  ._ |  
 | \| (_| |  | (_|  |_ | \/ (/_ | \| (/_ |_ \/\/ (_) |  |< 
```
[![GitHub license](https://img.shields.io/badge/License-MIT-blue.svg)](LICENSE)
[![Python 3.8](https://img.shields.io/badge/Python-3.8-yellow.svg)](https://www.python.org/)
[![NetworkX](https://img.shields.io/badge/NetworkX-3.1-green.svg)](https://networkx.org/)

A dynamic narrative generation system for AI-driven games, focusing on dramatic tension, conflict, and abstract world representation.

# Overview
NarrativeSphereAI is an experimental project creating emergent narratives through simulated agent interactions in a directed graph ecosystem. Unlike traditional simulations that focus on concrete geographical locations, we prioritize abstract representations to enhance dramatic potential. This framework serves as a backend for AI-native games, enabling dynamic story generation and character relationships.

## Key Features
- Graph-based narrative structure using networkx
- Agent-driven story evolution, emphasizing dramatic arcs
- Dynamic relationship mapping
- Emergent storytelling mechanics
- AI-native game integration capabilities

## Core Philosophy

We differentiate ourselves by focusing on:

- **Dramatic Tension and Conflict:** Our primary focus is on generating compelling narratives driven by dramatic tension and character conflict.
- **Abstract World Representation:** We abstract away from specific geographical locations, allowing for more flexible and impactful storytelling.
- **Counteracting the "Active Nihilism" of Everyday Life:** Games and narratives should combat the inherent fragmentation of human experience by providing engaging and meaningful experiences. We draw inspiration from the common origins of games and festivals in this regard. 
- **Leveraging LLM Token Representation:** Recognizing that LLMs can't fully capture game mechanics through natural language alone, we aim to utilize the abstract token representation of LLMs to create multi-layered game representations.
- **Synthetic Catallaxy:** We embrace the idea that game experience arises from the collision and coordination of the player's mental model and the game's world model, a concept Benjamin Bratton terms "synthetic catallaxy." We focus on synthetic (generated through non-mechanistic understanding) rather than artificial (simulating appearance) intelligence.

## Technical Foundation
- Built in Python
- Directed graph architecture
- Agent-based simluation.

## Use Cases
- Procedural narrative generation
- Dynamic game storytelling
- Character relationship simulation
- Interactive fiction backends
- AI-driven story worlds

# System Architecture

## System Components
### 1. Agent Layers
- **Base Layer (Directed Graph Ecosystem of Character)**
  - Directly embodies playable characters
  - Nodes maintain `character chains` containing:
    - Broadcast reception/submission records
    - Role prompts
    - Event participation history

- **Hidden Layer (Narrative Directors)**
  - Maintains `narrative chains` (one per Propp narrative type)
  - Each node specializes in specific narrative motifs
  - Controls dramatic progression through prompt interventions

- **Super Node (World Architect)**
  - Maintains single `world chain` tracking:
    - World state evolution blocks
    - Key narrative inflection points
    - Non-recurrent world properties
  - Ensures global narrative coherence and non-recurrence

### 2. Core Data Structures
- **World Chain**  
  Linear blockchain-like structure maintained by Super Node containing:
  - Timestamped world states
  - Major event summaries

- **Narrative Chains**  
  Multiple parallel chains (one per Propp archetype) containing:
  - Narrative progression markers
  - Character engagement levels
  - Genre-specific dramatic beats

- **Character Chains**  
  Per-agent chains storing:
  - Personal history fragments
  - Relationship dynamics
  - Psychological state vectors

- **Graph Ecosystem**  
  - Directed graph structure connecting all base layer nodes:
     * Base nodes are dominated by direct edges to other base nodes
	   - The dominating node can force other nodes to change the commit according to its requirements and access character chains of them
	 * Hidden layer nodes and super node have edges to all base nodes

## System Dynamics

### Initialization Phase
1. **Seed Activation**  
   - User provides initial world premise (seed prompt)
   - Super Node initializes world chain with genesis block

2. **World Priming**  
   - Super Node broadcasts seed to all layers
   - Generates 3-5 initial events using drama-weighted randomization
   - Targeted broadcast to p% of base layer nodes

3. **Character Emergence**  
   - Recipient nodes create own character chains
   - Submit character profiles to narrative chains

### Operational Cycle
1. **Lifecycle Management**  
   - Nodes inactive for 3 cycles get reset:
     * Clear character chain
     * Reinitialize from world chain state
     * Generate new role prompts

2. **Narrative Processing**  
   - Base nodes:
     * Combine character chain + received events
     * Generate event extensions (2-5 variations)
     * Submit to hidden layer via backward broadcast
	 * Ask to connect/dominate other base nodes(in a mutil-round conversation)

3. **Dramatic Curation**  
   - Hidden layer nodes:
     * Assess submissions against narrative type
     * Select top submissions per chain
     * Update narrative chains with new beats
     * Initiate new chains when arcs complete

4. **World Evolution**  
   - Super Node:
     * Analyzes all submissions using:
       - world state alignment
       - dramatic potential
       - novelty factor
     * Creates new world chain block
     * Generates 3-7 global events
     * Prioritizes broadcast to:
       * Key submission authors 
       * Newly reset nodes
       * Random nodes

5. **Feedback Loop**  
   - Event recipients update character chains
   - Hidden layer adjusts narrative weights
   - Super Node monitors dramatic entropy

# Getting Started
This project serves as a foundation for implementing dynamic narrative systems in games and interactive experiences. Detailed implementation guidelines and API documentation to follow.

## Initial Setup
Set up a Python environment and install the required dependencies from the `environment.yml` file.

```bash
conda env create -f environment.yml
```

Use the following command to activate the environment:

```bash
conda activate narrativeNetwork
```

## Seed and API Setup
Use `seed_config.json` to set up the initial seed prompt and API configuration.

```json
{
  "seed_prompt": "In a world where magic is forbidden, a young sorcerer discovers a hidden spellbook, and must decide whether to use its powers for good or evil.",
  "api_config": {
    "base_url": "https://api.deepseek.com",
    "api_key": "YOUR_API_KEY"
  }
}
```

## Running the System


[Additional documentation and setup instructions coming soon]

# License
This project is licensed under the MIT License - see the LICENSE file for details.

# Acknowledgments
- Inspiration from Propp's narrative theory.
- Utilization of the `networkx` library for graph representation.
- Philosophical insights from Benjamin Bratton's concept of synthetic catallaxy.