from datetime import datetime
def completed_in_fiscal_year(data, trainings, fiscal_year):
    fiscal_start = datetime(fiscal_year - 1, 7, 1)
    fiscal_end = datetime(fiscal_year, 6, 30)
    results = {training: [] for training in trainings}
    for entry in data:
        latest_completion = {}
        for completion in entry['completions']:
            name = completion['name']
            if name in trainings:
                completion_date = datetime.strptime(completion['timestamp'], '%m/%d/%Y')
                if name not in latest_completion or completion_date > latest_completion[name]['completion_date']:
                    latest_completion[name] = {'completion_date': completion_date}
        for name, completion_info in latest_completion.items():
            if fiscal_start <= completion_info['completion_date'] <= fiscal_end:
                results[name].append(entry['name'])
    return results
