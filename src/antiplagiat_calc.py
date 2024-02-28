import re

from AntiPlagiat.src.antiplagiat_utils import AntiPlagiat


class AntiPlagiatCalc:
    def __init__(self):
        self.jaccard = 0
        self.ast = 0
        self.sorenson = 0
        self.levenshtein = 0

    def _calc_jaccard(self, code_one, code_two):
        code_one = code_one.split("\n")
        code_two = code_two.split("\n")
        code_one = [line.strip() for line in code_one if line]
        code_two = [line.strip() for line in code_two if line]

        ap = AntiPlagiat()

        metric = ap.find_jaccard_similarity(code_one, code_two)
        self.jaccard = metric

        return metric

    def _calc_sorenson(self, code_one, code_two):
        metric = 0.2
        self.metric = 0.2
        return metric

    def _calc_ast(self):
        pass

    def calc_levenshtein(self, code_one, code_two):
        ap = AntiPlagiat()
        lev = ap.find_levenshtein("cat", "tac")
        # берем результат левенштейна, делим на количество символов в младшем коде, умножаем на 100%
        return lev

    def _calc_hash(self, code_one, code_two):
        pattern = "^[ ]{0,}#[\w|\W]{0,}\n$"
        code_one = re.sub(pattern, "", code_one)
        code_two = re.sub(pattern, "", code_two)
        ap = AntiPlagiat()
        if ap.find_hash(code_one, code_two):
            return True
        return False


apc = AntiPlagiatCalc()
one = """package main

import (
 "fmt"
)

var sbox = [0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76, 0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0, 0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15, 0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75, 0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84, 0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf, 0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8, 0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2, 0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73, 0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb, 0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79, 0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08, 0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a, 0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e, 0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf, 0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]byte{} // Removed extra space

func subBytes(state []byte) {
 for i := 0; i < len(state); i++ {
  state[i] = sbox[state[i]]
 }
}

func rotate(word []byte, n int) []byte {
 return append(word[n:], word[:n]...)
}

func shiftRows(state []byte) {
 for i := 0; i < 4; i++ {
  start := i * 4
  end := start + 4
  state[start:end] = rotate(state[start:end], i)
 }
}

func galoisMult(a, b byte) byte {
 p := byte(0)
 hiBitSet := byte(0)
 for i := 0; i < 8; i++ {
  if b&1 == 1 {
   p ^= a
  }
  hiBitSet = a & 0x80
  a <<= 1
  if hiBitSet == 0x80 {
   a ^= 0x1b
  }
  b >>= 1
 }
 return p
}

func mixColumn(column []byte) {
 temp := make([]byte, 4)
 copy(temp, column)

 column[0] = galoisMult(temp[0], 2) ^ galoisMult(temp[3], 1) ^ galoisMult(temp[2], 1) ^ galoisMult(temp[1], 3)
 column[1] = galoisMult(temp[1], 2) ^ galoisMult(temp[0], 1) ^ galoisMult(temp[3], 1) ^ galoisMult(temp[2], 3)
 column[2] = galoisMult(temp[2], 2) ^ galoisMult(temp[1], 1) ^ galoisMult(temp[0], 1) ^ galoisMult(temp[3], 3)
 column[3] = galoisMult(temp[3], 2) ^ galoisMult(temp[2], 1) ^ galoisMult(temp[1], 1) ^ galoisMult(temp[0], 3)
}

func mixColumnInv(column []byte) {
 temp := make([]byte, 4)
 copy(temp, column)

 column[0] = galoisMult(temp[0], 14) ^ galoisMult(temp[3], 9) ^ galoisMult(temp[2], 13) ^ galoisMult(temp[1], 11)
 column[1] = galoisMult(temp[1], 14) ^ galoisMult(temp[0], 9) ^ galoisMult(temp[3], 13) ^ galoisMult(temp[2], 11)
 column[2] = galoisMult(temp[2], 14) ^ galoisMult(temp[1], 9) ^ galoisMult(temp[0], 13) ^ galoisMult(temp[3], 11)
 column[3] = galoisMult(temp[3], 14) ^ galoisMult(temp[2], 9) ^ galoisMult(temp[1], 13) ^ galoisMult(temp[0], 11)
}

func addRoundKey(state, roundKey []byte) {
 for i := 0; i < len(state); i++ {
  state[i] ^= roundKey[i]
 }
}

func main() {
 state := []byte{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
 subBytes(state)
 fmt.Println("SubBytes: ", state)

 state = []byte{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
 shiftRows(state)
 fmt.Println("ShiftRows: ", state)

 g := []byte{1, 2, 3, 4}
 mixColumn(g)
 fmt.Println("MixColumn: ", g)

 state = []byte{1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16}
 roundKey := []byte{2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 1}
 addRoundKey(state, roundKey)
 fmt.Println("AddRoundKey: ", state)
}"""

two = """package main

import (
    "fmt"
    "strconv"
)

func expansion(keyPart []string) []string {
    var expendedKey []string = make([]string, 48)
    expansionTable := [48]int{31, 0, 1, 2, 3, 4, 3, 4, 5, 6, 7, 8, 7, 8, 9, 10, 11, 12, 11, 12, 13, 14, 15, 16, 15, 16, 17, 18, 19, 20, 19, 20, 21, 22, 23, 24, 23, 24, 25, 26, 27, 28, 27, 28, 29, 30, 31, 0,
    }

    for key, item := range expansionTable{
        expendedKey[key] = keyPart[item]
    }
    return expendedKey
}


func bitwise_xor(expendedKey []string) []string {
    var roundKey = []string{"1", "1", "1", "0", "0", "0", "0", "0", "1", "0", "1", "1", "1", "1", "1", "0", "0", "1", "1", "0", "0", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1", "0", "0", "1", "0", "1", "0", "1", "0", "1", "0", "1", "1", "1", "0", "0", "0"}
    var xoredExpendedKey []string = make([]string, 48)

    for key, value := range roundKey{
        keyPart, err := strconv.Atoi(value)

        if err != nil {
            panic(err)
        }

        expendedPart, err := strconv.Atoi(expendedKey[key])

        if err != nil {
            panic(err)
        }

        res := keyPart ^ expendedPart
        result := strconv.Itoa(res)
        xoredExpendedKey[key] = result
    }
    return xoredExpendedKey
}


func s_box_generation(xorResultKey []string) []string {

    var sBoxTableRow0 = [][]int{{0, 0, 14}, {0, 1, 4}, {0, 2, 13}, {0, 3, 1}, {0, 4, 2}, {0, 5, 15}, {0, 6, 11}, {0, 7, 8}, {0, 8, 3}, {0, 9, 10}, {0, 10, 6}, {0, 11, 12}, {0, 12, 5}, {0, 13, 9}, {0, 14, 0}, {0, 15, 7}}
    var sBoxTableRow1 = [][]int{{1, 0, 0}, {1, 1, 15}, {1, 2, 7}, {1, 3, 4}, {1, 4, 14}, {1, 5, 2}, {1, 6, 13}, {1, 7, 1}, {1, 8, 10}, {1, 9, 6}, {1, 10, 12}, {1, 11, 11}, {1, 12, 9}, {1, 13, 5}, {1, 14, 3}, {1, 15, 8}}
    var sBoxTableRow2 = [][]int{{2, 0, 4}, {2, 1, 1}, {2, 2, 14}, {2, 3, 8}, {2, 4, 13}, {2, 5, 6}, {2, 6, 2}, {2, 7, 11}, {2, 8, 15}, {2, 9, 12}, {2, 10, 9}, {2, 11, 7}, {2, 12, 3}, {2, 13, 10}, {2, 14, 5}, {2, 15, 0}}
    var sBoxTableRow3 = [][]int{{3, 0, 15}, {3, 1, 12}, {3, 2, 8}, {3, 4, 4}, {3, 5, 9}, {3, 6, 1}, {3, 7, 7}, {3, 8, 5}, {3, 9, 11}, {3, 10, 3}, {3, 11, 14}, {3, 12, 10}, {3, 13, 0}, {3, 14, 6}, {3, 15, 13}}

    var rowsStable = map[string][][]int{
        "0": sBoxTableRow0,
        "1": sBoxTableRow1,
        "2": sBoxTableRow2,
        "3": sBoxTableRow3,
    }
    var sBoxBase [][]string
    var slicesIndx []int
    var output []string
    length := len(xorResultKey)
    foo := 0
    bar := 0
    for foo < length-1{
        foo += 6
        slicesIndx = append(slicesIndx, foo)
    }
    for _, value := range slicesIndx {
        sliceXor := xorResultKey[bar:value]
        sBoxBase = append(sBoxBase, sliceXor)
        bar = value
    }
    var finalBox [][]int

    for _, value := range sBoxBase{
        var newSBox []int
        string_position := value[0] + value[5]
        column_position := value[1] + value[2] + value[3] + value[4]

        decimal_string, err := strconv.ParseInt("0b" + string_position, 0, 64)

        if err != nil {
            panic(err)
        }

        decimal_column, err := strconv.ParseInt("0b" + column_position, 0, 64)

        if err != nil {
            panic(err)
        }

        map_position := strconv.Itoa(int(decimal_string))
        currentSBox := rowsStable[map_position]

        // можно через хешмап, но это перегруз вложенности!
        var to_change int
        for key, _ := range currentSBox {
            if int(decimal_column) == currentSBox[key][1] {
                to_change = currentSBox[key][2]
                newSBox = append(newSBox, to_change)
            }
        }
        finalBox = append(finalBox, newSBox)
    }
    for key, _ := range finalBox {
        binary_value := strconv.FormatInt(int64(finalBox[key][0]), 2)

        if len(binary_value) < 4 {
            for len(binary_value) < 4 {
                binary_value = "0" + binary_value
            }
        }
        for key, _ := range string(binary_value) {
            output = append(output, string(binary_value[key]))
        }
    }
    return output

}

func permutation(sBox[]string) []string{
    var permutatedKey []string = make([]string, 32)
    permutationTable := [32]int{15, 6, 19, 20, 28, 11, 27, 16, 0, 14, 22, 25, 4, 17, 30, 9, 1, 7, 23, 13, 31, 26, 2, 8, 18, 12, 29, 5, 21, 10, 3, 24}

    for key, item := range sBox{
        permutatedKey[permutationTable[key]] = item
    }
    return permutatedKey
}

func main () {
    var key = []string{"0", "0", "0", "0", "0", "0", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "0", "0", "1", "0", "1", "0", "1", "0", "0", "1", "1", "1", "0", "0", "1", "1",
    }
    expended := expansion(key)
    fmt.Println(expended)
    xored := bitwise_xor(expended)
    fmt.Println(xored)
    sboxed := s_box_generation(xored)
    fmt.Println(sboxed)
    permutated := permutation(sboxed)
    fmt.Println(permutated)
}"""

print(apc.calc_levenshtein(one, two))
