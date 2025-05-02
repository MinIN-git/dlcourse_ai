def binary_classification_metrics(prediction, ground_truth):
    '''
    Computes metrics for binary classification

    Arguments:
    prediction, np array of bool (num_samples) - model predictions
    ground_truth, np array of bool (num_samples) - true labels

    Returns:
    precision, recall, f1, accuracy - classification metrics
    '''
    
    # TODO: implement metrics!
    # Some helpful links:
    # https://en.wikipedia.org/wiki/Precision_and_recall
    # https://en.wikipedia.org/wiki/F1_score

    tp, fp, fn, tn = 0, 0, 0, 0

    count = len(prediction)
    for i in range(count):
        if prediction[i] and ground_truth[i]:
            tp += 1
        elif prediction[i] and not(ground_truth[i]):
            fp += 1
        elif not(prediction[i]) and not(ground_truth[i]):
            tn += 1
        elif not(prediction[i]) and ground_truth[i]:
            fn += 1
        else:
            print(prediction[i], ground_truth[i])
    
    if (tp + fp + tn + fn) != count:
        raise "Bad confusion matrix"

    precision = tp / (tp + fp)
    recall = tp / (tp + fn)
    accuracy = (tp + tn) / (tp + tn + fp + fn)
    f1 = 2 * (precision * recall) / (precision + recall)
    
    return precision, recall, f1, accuracy


def multiclass_accuracy(prediction, ground_truth):
    '''
    Computes metrics for multiclass classification

    Arguments:
    prediction, np array of int (num_samples) - model predictions
    ground_truth, np array of int (num_samples) - true labels

    Returns:
    accuracy - ratio of accurate predictions to total samples
    '''
    
    # TODO: Implement computing accuracy
    count = len(prediction)
    good_pred = 0
    
    for i in range(count):
        if prediction[i] == ground_truth[i]:
            good_pred += 1

    
    accuracy = good_pred / count

    return accuracy
