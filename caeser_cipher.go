package main

import (
	"fmt"
)

func encrypt(text string, shift int) string {
	result := ""

	for i := 0; i < len(text); i++ {
		char := text[i]

		if char >= 'A' && char <= 'Z' {
			encryptedChar := (int(char) + shift - 65) % 26 + 65
			result = result + string(rune(encryptedChar))
		} else if char >= 'a' && char <= 'z' {
			encryptedChar := (int(char) + shift - 97) % 26 + 97
			result = result + string(rune(encryptedChar))
		} else {
			result = result + string(char)
		}
	}

	return result
}

func main() {
	var text string
	var shift int

	fmt.Println("Enter the text string to encrypt: ")
	fmt.Scanln(&text)

	fmt.Println("Enter the shift value: ")
	fmt.Scanln(&shift)

	fmt.Println("Text: ", text)
	fmt.Println("Shift: ", shift)
	fmt.Println("Cipher: ", encrypt(text, shift))
}

