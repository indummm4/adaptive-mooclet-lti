from .algorithms import computeExplanation_Thompson
from .models import Explanation, Result
import random


def get_explanation_for_student(answer, user, method):

    explanations = answer.explanation_set.all()

    if method == 'thompson':

        allExplanations = []
        allResultsForExplanations = []
        for explanation in explanations:
            someResults = []
            for result in explanation.result_set.all():
                someResults.append(result.value)
            allResultsForExplanations.append(someResults)
            allExplanations.append(explanation)
        student_id = 'placeholder'
        selectedExplanation, exp_value = computeExplanation_Thompson(student_id, allExplanations, allResultsForExplanations)
        return selectedExplanation

    elif method == 'random':
        return random.choice(explanations)

    else:
        raise Exception('Method "{}" for determining explanation not recognized')