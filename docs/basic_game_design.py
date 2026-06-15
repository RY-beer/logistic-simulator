# this file describes the basic game design

GAME = {
    "name": "Mini Logistics World",

    "core_loop": [
        "generate_orders",
        "assign_tasks",
        "move_agents",
        "pickup_cargo",
        "deliver_cargo",
        "update_world_state"
    ],

    "design_goal": [
        "resource optimization under constraints",
        "multi-agent task scheduling",
        "emergent logistics efficiency problems"
    ]
}

WORLD = {
    "grid": {
        "type": "2D",
        "size": "configurable",
        "movement_cost_model": "manhattan"
    },

    "time": {
        "type": "tick_based",
        "tick_duration": "configurable"
    }
}

CARGO_SYSTEM = {
    "properties": [
        "weight",
        "volume",
        "cargo_type",
        "tags",
        "temperature_requirement",
        "fragility_level",
        "stack_group"
    ],

    "temperature_levels": [
        "NONE",
        "COOL",
        "COLD",
        "FROZEN",
        "HEATED"
    ],

    "design_intent": [
        "all constraints must be extensible without schema change",
        "tags are primary expansion mechanism for future rules"
    ]
}

CONSTRAINT_SYSTEM = {
    "constraint_types": [
        "INCOMPATIBLE_WITH",
        "MUST_BE_ALONE",
        "REQUIRES_TEMPERATURE",
        "MAX_COUNT",
        "MAX_WEIGHT",
        "MAX_VOLUME"
    ],

    "rule_model": {
        "scope": "cargo / truck / global",
        "target": "tag | cargo_type | stack_group",
        "value": "parameter dependent on rule type"
    },

    "design_intent": [
        "rules are data-driven, not hardcoded",
        "future difficulty increases come from adding rules only"
    ]
}

TRUCK_SYSTEM = {
    "truck_types": [
        "STANDARD",
        "REFRIGERATED",
        "HEAVY",
        "FRAGILE_HANDLING",
        "EXPRESS"
    ],

    "properties": [
        "capacity_weight",
        "capacity_volume",
        "supported_temperature",
        "allowed_tags",
        "current_load",
        "location",
        "status"
    ],

    "design_intent": [
        "truck type defines constraint envelope",
        "upgrade system possible via new truck types only"
    ]
}

SUPPLIER_SYSTEM = {
    "properties": [
        "location",
        "production_rate",
        "available_cargo_types",
        "reliability"
    ],

    "design_intent": [
        "suppliers act as stochastic generators of logistics demand",
        "future expansion: dynamic economy simulation"
    ]
}

ORDER_SYSTEM = {
    "design_intent": [
        "orders define optimization pressure",
        "priority + time window = difficulty scaling knobs"
    ]
}

TASK_SYSTEM = {
    "task_types": [
        "PICKUP",
        "DELIVER",
        "REPOSITION",
        "WAIT"
    ],

    "design_problem": [
        "task assignment is global optimization problem",
        "local greedy selection is intentionally insufficient at scale"
    ]
}

AGENT_SYSTEM = {
    "design_intent": [
        "all moving entities follow same abstraction",
        "drones are just low-capacity fast agents"
    ]
}

TASK_ASSIGNMENT = {
    "goal": "assign best task to each agent each tick",

    "naive_model": [
        "choose nearest task"
    ],

    "intended_model_evolution": [
        "distance heuristic",
        "weighted scoring function",
        "constraint-aware scoring",
        "auction system",
        "global optimization (future)"
    ],

    "score_factors": [
        "distance",
        "urgency",
        "compatibility",
        "penalty avoidance",
        "agent specialization bonus"
    ]
}

GAME_LOOP = {
    "tick_flow": [
        "generate_orders",
        "generate_tasks",
        "score_tasks",
        "assign_tasks",
        "move_agents",
        "execute_actions",
        "resolve_constraints",
        "update_world_state"
    ]
}

DESIGN_PRINCIPLES = {
    "rules_not_code": True,

    "extensibility_first": [
        "new difficulty comes from new constraints",
        "not from rewriting algorithms"
    ],

    "everything_is_scoreable": True,

    "avoid_local_greedy_only": True,

    "system_should_emerge_complexity": True
}