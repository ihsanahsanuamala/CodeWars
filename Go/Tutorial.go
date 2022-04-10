package main

import "fmt"

// Switch Case
// func main() {
// 	age := 19
// 	switch age {

// 	case 15:
// 		fmt.Println("Masih Kecil")
// 	case 16:
// 		fmt.Println("Juga Masih Kecil")
// 	case 17:
// 		fmt.Println("Masih Kecil Juga Ngab")
// 	case 18:
// 		fmt.Println("Mulai Gede")
// 	case 19:
// 		fmt.Println("Nah ini baru matang")
// 	default:
// 		fmt.Println("Ketuaan Ngab")

// 	}
// }

func main() {
	var EvenNum [5]int
	EvenNum[0] = 1
	EvenNum[1] = 2
	EvenNum[2] = 3
	EvenNum[3] = 4
	EvenNum[4] = 5
	// fmt.Println(EvenNum[2])
	fmt.Println(EvenNum)

	// for i := 0; i < len(EvenNum); i++ {
	// 	if EvenNum[i]%2 == 0 {
	// 		fmt.Println(EvenNum[i])
	// 	}
	// }
	for _, value := range EvenNum {

		fmt.Println(value)
	}
}
