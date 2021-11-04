#El método merge divide la lista en mitades para luego ordenar estas mitades
#Los llamados recursivos hacen que la mitad se vuelva a dividir en mitades


#Comenzando con la lista de 16 elementos
[21, 1, 26, 45, 29, 28, 2, 9, 16, 49, 39, 27, 43, 34, 46, 40] 

#El primer llamado recursivo la divide en listas de 8 elementos, el segundo en listas de 4 y el tercero en listas de 2 elementos
[[21,1] [26,45] [29,28] [2,9] [16,49] [39,27] [43,34] [46,40]]

#Y finalmente ordenará todas estas sublistas, 
[[1,21] [26,45] [28,29] [2,9] [16,49] [27,39] [34,43] [40,46]]