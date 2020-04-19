from FAE.FeatureAnalysis.Normalizer import *
from FAE.FeatureAnalysis.DimensionReduction import *
from FAE.FeatureAnalysis.FeatureSelector import *
from FAE.FeatureAnalysis.Classifier import *
from FAE.FeatureAnalysis.CrossValidation import *

from copy import deepcopy

class Index2Dict:
    def __init__(self):
        pass

    def GetInstantByIndex(self, name):

        if name == NormalizerNone.GetName():
            return NormalizerNone
        elif name == NormalizerUnit.GetName():
            return NormalizerUnit
        elif name == NormalizerZeroCenter.GetName():
            return NormalizerZeroCenter
        elif name == NormalizerZeroCenterAndUnit.GetName():
            return NormalizerZeroCenterAndUnit
        elif name == DimensionReductionByPCA().GetName():
            return DimensionReductionByPCA()
        elif name == 'Cos':
            return DimensionReductionByPCC()
        elif name == DimensionReductionByPCC().GetName():
            return DimensionReductionByPCC()
        elif name == FeatureSelectByRelief().GetName():
            return FeatureSelectByRelief()
        elif name == FeatureSelectByANOVA().GetName():
            return FeatureSelectByANOVA()
        elif name == FeatureSelectByRFE().GetName():
            return FeatureSelectByRFE()
        elif name == FeatureSelectByMrmr().GetName():
            return FeatureSelectByMrmr()
        elif name == SVM().GetName():
            return SVM()
        elif name == LDA().GetName():
            return LDA()
        elif name == AE().GetName():
            return AE()
        elif name == RandomForest().GetName():
            return RandomForest()
        elif name == DecisionTree().GetName():
            return DecisionTree()
        elif name == AdaBoost().GetName():
            return AdaBoost()
        elif name == NaiveBayes().GetName():
            return NaiveBayes()
        elif name == GaussianProcess().GetName():
            return GaussianProcess()
        elif name == LR().GetName():
            return LR()
        elif name == LRLasso().GetName():
            return LRLasso()
        elif name == CrossValidationLeaveOneOut().GetName():
            return CrossValidationLeaveOneOut()
        elif name == CrossValidation5Folder().GetName():
            return CrossValidation5Folder()
        elif name == CrossValidation10Folder().GetName():
            return CrossValidation10Folder()