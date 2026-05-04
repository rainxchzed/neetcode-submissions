class Solution {

    fun encode(strs: List<String>): String {
        if(strs.isEmpty()) return ""
        if(strs.size == 1 && strs[0] == "") return "empty"
        return strs.joinToString("..,. ")
    }

    fun decode(str: String): List<String> {
        if(str.isEmpty()) return listOf()
        if(str == "empty") return listOf("")
        return str.split("..,. ")
    }
}
