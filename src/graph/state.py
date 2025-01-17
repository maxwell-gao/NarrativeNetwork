import json


class WorldState:
    """
    Represents the state of the world, including information flow, dominance relationships,
    agent states, global events, and world resources.
    """

    def __init__(self, info_flow=None, dominance=None, agent_states=None, global_events=None, world_resources=None):
        """
        Initialize a new WorldState.

        :param info_flow: A dictionary representing information flow between agents.
        :param dominance: A dictionary representing dominance relationships between agents.
        :param agent_states: A dictionary representing the state of each agent.
        :param global_events: A list of global events affecting the world.
        :param world_resources: A dictionary representing world resources.
        """
        self.info_flow = info_flow if info_flow is not None else {}
        self.dominance = dominance if dominance is not None else {}
        self.agent_states = agent_states if agent_states is not None else {}
        self.global_events = global_events if global_events is not None else []
        self.world_resources = world_resources if world_resources is not None else {}

    def to_json(self):
        """
        Serialize the world state to a JSON string.

        :return: A JSON string representing the world state.
        """
        return json.dumps({
            "info_flow": self.info_flow,
            "dominance": self.dominance,
            "agent_states": self.agent_states,
            "global_events": self.global_events,
            "world_resources": self.world_resources
        }, indent=4)

    @classmethod
    def from_json(cls, json_str):
        """
        Deserialize a JSON string into a WorldState object.

        :param json_str: A JSON string representing the world state.
        :return: A WorldState object.
        """
        data = json.loads(json_str)
        return cls(
            info_flow=data.get("info_flow", {}),
            dominance=data.get("dominance", {}),
            agent_states=data.get("agent_states", {}),
            global_events=data.get("global_events", []),
            world_resources=data.get("world_resources", {})
        )

    def update(self, info_flow=None, dominance=None, agent_states=None, global_events=None, world_resources=None):
        """
        Update the world state with new data.

        :param info_flow: A dictionary to update the information flow.
        :param dominance: A dictionary to update the dominance relationships.
        :param agent_states: A dictionary to update the agent states.
        :param global_events: A list to update the global events.
        :param world_resources: A dictionary to update the world resources.
        """
        if info_flow is not None:
            self.info_flow.update(info_flow)
        if dominance is not None:
            self.dominance.update(dominance)
        if agent_states is not None:
            self.agent_states.update(agent_states)
        if global_events is not None:
            self.global_events.extend(global_events)
        if world_resources is not None:
            self.world_resources.update(world_resources)

    def __repr__(self):
        """
        Return a string representation of the world state.
        """
        return (f"WorldState(info_flow={self.info_flow}, dominance={self.dominance}, "
                f"agent_states={self.agent_states}, global_events={self.global_events}, "
                f"world_resources={self.world_resources})")
