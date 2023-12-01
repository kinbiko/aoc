package aoc

import (
	"strconv"
	"strings"
	"testing"
)

func TestDay01(t *testing.T) {
	t.Run("part 1", func(t *testing.T) {
		if sum, want := part1(ex1), 142; sum != want {
			t.Errorf("want: %d, got: %d", want, sum)
		}
		if sum, want := part1(in), 56042; sum != want {
			t.Errorf("want: %d, got: %d", want, sum)
		}
	})

	t.Run("part 2", func(t *testing.T) {
		if sum, want := part2(ex2), 281; sum != want {
			t.Errorf("want: %d, got: %d", want, sum)
		}
		if sum, want := part2(in), 55358; sum != want {
			t.Errorf("want: %d, got: %d", want, sum)
		}
	})
}

func part1(in string) int {
	sum := 0
	for _, row := range strings.Split(in, "\n") {
		digits := map[string]string{"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9"}
		left := findLeftmostNumber(row, digits)
		right := findLeftmostNumber(reverse(row), digits)
		n, _ := strconv.Atoi(left + right)
		sum += n
	}
	return sum
}

func part2(in string) int {
	sum := 0
	for _, row := range strings.Split(in, "\n") {
		left := findLeftmostNumber(row, map[string]string{
			"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
			"zero": "0", "one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9",
		})
		right := findLeftmostNumber(reverse(row), map[string]string{
			"1": "1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9",
			"orez": "0", "eno": "1", "owt": "2", "eerht": "3", "ruof": "4", "evif": "5", "xis": "6", "neves": "7", "thgie": "8", "enin": "9",
		})
		n, _ := strconv.Atoi(left + right)
		sum += n
	}
	return sum
}

func findLeftmostNumber(s string, str2Digit map[string]string) string {
	for i := range s {
		for number := range str2Digit {
			if strings.HasPrefix(s[i:], number) {
				return str2Digit[number]
			}
		}
	}
	return ""
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}
