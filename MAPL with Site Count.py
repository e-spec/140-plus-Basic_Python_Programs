import math

def compare_frequencies():
    print("--- 5G WTTH: 700MHz vs 3.5GHz Comparison ---")
    target_area_sq_km = 1000
    
    # Shared Specs
    tx_power = 46; tx_gain = 18; rx_gain = 16
    rsrp_threshold = -105
    
    # Frequency Specifics [Frequency (MHz), Foliage Loss (dB)]
    scenarios = [
        {"name": "Rural 700MHz", "freq": 700, "foliage": 3.0},
        {"name": "Urban/Mid 3.5GHz", "freq": 3500, "foliage": 20.0} # 20dB loss for trees/buildings
    ]

    for sc in scenarios:
        # Corrected MAPL Calculation
        # Total Budget = Power + Gains + Absolute Threshold - Environmental Loss
        mapl = (tx_power + tx_gain + rx_gain + abs(rsrp_threshold)) - sc["foliage"]
        
        # Calculate Theoretical Radius
        log_f = 20 * math.log10(sc["freq"])
        log_d = (mapl - log_f - 32.44) / 20
        raw_radius = 10**log_d
        
        # Reality Clamp (Earth Curvature)
        planned_radius = min(raw_radius, 18.0)
        
        # Coverage Area
        site_area = 2.6 * (planned_radius**2)
        num_sites = math.ceil(target_area_sq_km / site_area)
        
        print(f"\nScenario: {sc['name']}")
        print(f"  Effective MAPL:  {mapl:.2f} dB")
        print(f"  Foliage Loss:    {sc['foliage']} dB")
        print(f"  Planned Radius:  {planned_radius:.2f} km")
        print(f"  Sites needed for {target_area_sq_km} sq km: {num_sites}")

if __name__ == "__main__":
    compare_frequencies()