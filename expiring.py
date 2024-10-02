from datetime import datetime, timedelta
def expired_or_expires_soon(data, reference_date):
    reference_date = datetime.strptime(reference_date, '%Y-%m-%d')
    soon_threshold = reference_date + timedelta(days=30)
    expiring_status = []
    for entry in data:
        person_info = {'name': entry['name'], 'trainings': []}
        latest_completion = {}
        for completion in entry['completions']:
            name = completion['name']
            if completion['expires']:
                expiration_date = datetime.strptime(completion['expires'], '%m/%d/%Y')
                if name not in latest_completion or expiration_date > latest_completion[name]['expiration_date']:
                    latest_completion[name] = {
                        'completion_date': datetime.strptime(completion['timestamp'], '%m/%d/%Y'),
                        'expiration_date': expiration_date
                    }
        for name, dates in latest_completion.items():
            expiration_date = dates['expiration_date']
            if expiration_date < reference_date:
                status = 'expired'
            elif reference_date <= expiration_date <= soon_threshold:
                status = 'expires soon'
            else:
                continue
            person_info['trainings'].append({
                'training_name': name,
                'expiration_date': expiration_date.strftime('%m/%d/%Y'),
                'status': status
            })
        if person_info['trainings']:
            expiring_status.append(person_info)
    return expiring_status
