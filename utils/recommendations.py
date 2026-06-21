def generate_recommendations(
    risk,
    event_cause,
    event_type,
    zone,
    corridor
):

    recommendations = []

    # =========================
    # BASED ON RISK LEVEL
    # =========================

    if risk == "High":

        recommendations += [
            "🚨 Activate Emergency Traffic Protocol",
            "👮 Deploy Maximum Traffic Personnel (6–10)",
            "🚧 Install Temporary Barricades",
            "📢 Issue Immediate Public Advisory"
        ]

    elif risk == "Low":

        recommendations += [
            "👮 Deploy 1–3 Traffic Personnel",
            "🚧 Minimal Barricades Required",
            "📢 Routine Monitoring Only"
        ]

    # =========================
    # EVENT CAUSE LOGIC
    # =========================

    cause_map = {

        "accident": [
            "🚑 Dispatch Ambulance & Rescue Team",
            "🚓 Alert Nearby Police Units"
        ],

        "vehicle_breakdown": [
            "🔧 Arrange Breakdown Recovery Vehicle",
            "🚧 Clear Lane Quickly"
        ],

        "public_event": [
            "🎤 Coordinate with Event Organizers",
            "🚌 Manage Crowd Flow & Parking"
        ],

        "protest": [
            "🚨 High Alert Zone Setup",
            "👮 Extra Security Deployment"
        ],

        "construction": [
            "🛑 Temporary Diversion Setup",
            "⚠ Install Work Zone Signage"
        ],

        "water_logging": [
            "🌧 Drainage Clearance Team",
            "🚧 Block Affected Road Section"
        ],

        "vip_movement": [
            "🚔 Secure VIP Route",
            "📡 Real-time Surveillance"
        ]
    }

    if event_cause in cause_map:

        recommendations += cause_map[event_cause]

    # =========================
    # ZONE INTENSITY LOGIC
    # =========================

    if zone in ["Central Zone 1", "Central Zone 2"]:

        recommendations.append(
            "🏙 High-density Zone → Expect Heavy Congestion"
        )

    # =========================
    # CORRIDOR LOGIC
    # =========================

    if "ORR" in corridor or "Ring Road" in corridor:

        recommendations.append(
            "🛣 Major Corridor → Enable Dynamic Signal Control"
        )

    # Remove duplicates
    recommendations = list(set(recommendations))

    return recommendations