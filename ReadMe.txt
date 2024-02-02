
File: Binary_Hamming_distance_substitution.py
This file contains an implementation of binary ReLU network to 
generate strings with a given Hamming distance. 

Input: 
		e := Input string of length n
		d := Hamming distance
		x := The binary conversion string of length n
Output:  
		y := The string obtained by applying substitution operation
				on e following x and has at most distance d. 

An example 
		e = [1,1,0]
		d = 2
		x = [1, 3]
Output: y = [0, 1, 1]	

###################################################
File: Hamming_distance_substitution.py
This file contains an implementation of the ReLU network to 
generate strings with a given Hamming distance. 

Input: 
		e := Input string of length n
		d := Hamming distance
		m := The size of the symbol set
		x := The conversion string of length 2n
Output:  
		y := The string obtained by applying substitution operation
				on e following x and has at most distance d. 

An example 
		e = [4,1, 3, 2]
		d = 3
		m = 5
		x = [2, 4, 2, 5, 1, 3]
Output: y = [4, 5, 3, 1]

####################################################
File: Edit_distance_deletion.py
This file contains an implementation of the ReLU network to 
generate strings with a given edit distance due to deletion 
operation only. 

Input: 
		e := Input string of length n
		d := Hamming distance
		x := The conversion string of length n
Output:  
		y := The string obtained by applying deletion operation
				on e following x and has at most distance d. 

An example 
		e := [3, 2, 4, 1]
		d := 2
		x := [1, 3]
Output:
		y := [2, 1]

########################################################
File: Edit_distance_insertion.py
This file contains an implementation of the ReLU network to 
generate strings with a given edit distance due to insertion 
operation only. 

Input: 
		e := Input string of length n
		d := Edit distance
		m := The size of the symbol set
		x := The conversion string of length 2n
Output:  
		y := The string obtained by applying insertion operation
				on e following x and has at most distance d. 

An example 
		e = [3, 2, 4, 1]
		d = 3
		m = 5
		x = [4, 1, 4, 3, 2, 5]
Output: y = [2, 3, 2, 4, 3, 5, 1]

########################################################
File: Edit_distance_unified.py
This file contains an implementation of the ReLU network to 
generate strings with a given edit distance due to substitution,
deletion and insertion operations simultaneously. 

Input: 
		e := Input string of length n
		d := Edit distance
		m := The size of the symbol set
		Delta := The small number
		x := The conversion string of length 2n
Output:  
		y := The string obtained by applying substiution, deletion, 
			 and operation simultaneously on e following x and 
			 has at most distance d. 

An example 
		e: [4, 1, 3, 7, 5]
		m: 7
		d: 3
		Delta: 0.01
		x: [0.03, 0, 0.03, 0.27, 0, 0.6, 0, 0.55, 0.55, 0, 
		0.25, 0.9, 0, 0.7, 0.24]
Output: y = [2, 5, 1, 3, 5]

########################################################