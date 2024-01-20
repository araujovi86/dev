#pacman app & mongodb

#The deploy will create an application and db, which can be used to test storage.
#After play the game, save your score. This will update the db with statics and can be checked trough application ui.

#Don't forget to update the namespace name from kustomization.yaml with target namespace and the pvc with target storageClass.

#clone the repo
git clone https://git-eagle.siemens.com/openshift1/ocp-scripts.git

#check the files
kubectl kustomize ./pacman

#apply the kustomization
oc apply -k ./pacman

#Enjoy :)
