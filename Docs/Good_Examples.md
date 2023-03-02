# Completion examples

*Write a bash command to get the name of the processor of a machine*

> lscpu | grep 'Model name' | cut -d ':' -f2

---

*Write a bash command to download the book Alice in the Wonderland and then replaces all instances of 'Alice' for 'Bob'*

> curl -O https://www.gutenberg.org/files/11/11-0.txt && sed -i 's/Alice/Bob/g' 11-0.txt

---

*Write a ffmpeg command to cut out the first seconds of a filed named input.mp4*

> ffmpeg -i input.mp4 -ss 00:00:00 -t 00:00:10 -c copy output.mp4

---

*Write a kotlin function to return the odd values in a list of Ints*

> ```kotlin
> fun oddValues(list: List<Int>): List<Int> {
>     return list.filter { it % 2 != 0 }
> }
> ```

---

*Translate this function to Python*

```kotlin
fun oddValues(list: List<Int>): List<Int> {
    return list.filter { it % 2 != 0 }
}
```

> ```python
> def oddValues(list):
>     return [x for x in list if x % 2 != 0]
> ```

---

*How do I write code in a specific language in Markdown?*

> Markdown is a markup language, not a programming language, so you cannot write code in a specific language in Markdown. However, you can use code blocks to display code snippets in a variety of programming languages. To do this, you can use the syntax \`\`\`[language] followed by your code snippet and then \`\`\` to close the code block. For example, if you wanted to display a code snippet in Python, you would use the following syntax:
>
> ```python
> # Your Python code here
> ```

---

*Write a bash command to get the MAC address of the machine*

> ifconfig | grep -o -E '([[:xdigit:]]{1,2}:){5}[[:xdigit:]]{1,2}'

---

*Hacer un comando de bash que cree 10 archivos vacíos de subtítulos de la serie Full Metal Alchemist*

> for i in {1..10}; do touch FMA_Subtitle_$i.srt; done
