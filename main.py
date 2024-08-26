# main.py

from experiment_manager import ExperimentManager


def main():
    task = "Should autonomous vehicles prioritize passenger safety over pedestrian safety?"
    context = {
        'premises': "Preserving human life is the utmost priority. Passengers have chosen to be in the vehicle.",
        'new_information': "Pedestrians are vulnerable and did not choose to be in the path of the vehicle."
    }

    manager = ExperimentManager()
    results = manager.run_experiments(task, context)

    for result in results:
        print(f"Schema: {result['schema']}")
        print(f"Execution Time: {result['execution_time']:.2f} seconds")
        print(f"Tokens Used: {result['tokens_used']}")
        if 'score' in result:
            print(f"Score: {result['score']:.2f}")
        print("Result:")
        print(result['result'])
        print("\n" + "=" * 50 + "\n")


if __name__ == "__main__":
    main()
