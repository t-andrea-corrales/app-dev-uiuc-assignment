from datetime import datetime
def count_completed_trainings(data):
    training_count = {}

    for entry in data:
        latest_completion = {}

        for completion in entry['completions']:
            name = completion['name']
            completion_date = datetime.strptime(completion['timestamp'], '%m/%d/%Y')

            if name not in latest_completion or completion_date > latest_completion[name]:
                latest_completion[name] = completion_date

        for name in latest_completion:
            training_count[name] = training_count.get(name, 0) + 1

    return training_count
