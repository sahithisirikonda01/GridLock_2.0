from utils.predictor import predict_risk

result = predict_risk(
    event_type="planned",
    event_cause="public_event",
    corridor="CBD 1",
    police_station="Cubbon Park",
    zone="Central Zone 1",
    junction="TrinityCircle"
)

print("\nPredicted Risk:", result)