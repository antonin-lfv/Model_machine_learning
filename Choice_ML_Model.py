"""" SKlearn algorithm cheat-sheet """

import time

## Choose a model

def model_choice_sklearn():
    print('* answer by yes or no : ')
    time.sleep(1)
    if input('nb_samples >50 :' ) == 'no':
        print('-------------------------')
        print('● Get more data !')
    elif input('predicting a category :') == 'no' :
        if input('predicting a quantity :') == 'no' :
            if input('just looking :') == 'no' :
                    print('● Tough luck !')
            else :
                print('● Welcome in dimensionality reduction !')
                print('-------------------------')
                print('● Your modele : Randomized PCA')
                print('-------------------------')
                print('● If not working :')
                if input('samples <10K :') == 'no':
                    print('-------------------------')
                    print('● Your modele : Kernel approximation')
                else :
                    print('-------------------------')
                    print('● Your modeles : Isomap or SpectralEmbedding')
                    print('-------------------------')
                    print('● If no working : LLE ')
        else :
            print('● Welcome in regression')
            if input('samples <100K :')=='no':
                print('-------------------------')
                print('● Your modele : SGD Regressor !')
            elif input('few features should be important :') == 'yes':
                print('-------------------------')
                print('● Your modeles : Lasso or ElasticNet ')
            else :
                print('-------------------------')
                print('● Your modeles : SVR(kernel = "linear") or RidgeRegression ')
                print('-------------------------')
                print('● If not working : EnsembleRegressors or SVR(kernel="rbf") ')
    elif input('do you have labeled data ? :') == 'no' :
        print('● Welcome in Clustering !')
        if input('number of categories known :') == 'no' :
            if input('samples <10K :') == 'no' :
                print('● Tough luck !')
            else :
                print('-------------------------')
                print('● Your modeles : MeanShift or VBGMM ')
        elif input('samples <10K :') == 'no':
            print('-------------------------')
            print('● Your modele : MiniBatchKMeans ')
        else :
            print('-------------------------')
            print('● Your modele : KMeans ')
            print('-------------------------')
            print('● If not working : SpectralClustering or GMM ')
    else :
        print('● Welcome in classification !')
        if input('samples <100k :') == 'no' :
            print('-------------------------')
            print('● Your modele : SGDClassifier ')
            print('-------------------------')
            print('● If not working : Kernel approximation ')
        else :
            print('-------------------------')
            print('● Your modele : LinearSVC ')
            print('-------------------------')
            print('● If not working :')
            if input('Text data :')=='yes':
                print('-------------------------')
                print('● Your modele : NaiveBayes')
            else :
                print('-------------------------')
                print('● Your modele : KNeighborsClassifier')
                print('-------------------------')
                print('● If not working : SVC or EnsembleClassifiers')
    print('Finished!')









