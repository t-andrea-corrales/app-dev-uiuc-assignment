import json
from trainings import count_completed_trainings
from fiscal import completed_in_fiscal_year
from expiring import expired_or_expires_soon
def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)
def export_to_txt(file_name, data):
    with open(file_name, 'w') as f:
        f.write(json.dumps(data, indent=4))
def main():
    file_path = 'trainings.txt'
    data = load_data(file_path)

    print("Part 1: Training Completion Counts")
    completed_count = count_completed_trainings(data)
    print(json.dumps(completed_count, indent=4))
    export_to_txt('trainings-outputt.txt', completed_count)
    print("\nPart 2: People who completed specified trainings in FY 2024")
    trainings_list = ["Electrical Safety for Labs", "X-Ray Safety", "Laboratory Safety Training"]
    fiscal_year = 2024
    fiscal_results = completed_in_fiscal_year(data, trainings_list, fiscal_year)
    print(json.dumps(fiscal_results, indent=4))
    export_to_txt('fiscalyear-complete-output.txt', fiscal_results)
    print("\nPart 3: Expired or Soon-to-Expire Trainings")
    reference_date = '2024-09-01'  # Example date
    expiring_results = expired_or_expires_soon(data, reference_date)
    print(json.dumps(expiring_results, indent=4))
    export_to_txt('expiring-output.txt', expiring_results)

if __name__ == "__main__":
    main()