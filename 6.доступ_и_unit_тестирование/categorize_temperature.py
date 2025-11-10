def categorize_temperature(temp):
    if temp <= 0: return 'freezing'

    elif 0 < temp <= 10: return 'cold'

    elif 10 < temp <= 20: return 'cool'

    elif 20 < temp <= 30: return 'warm'

    elif temp > 30: return 'hot'
