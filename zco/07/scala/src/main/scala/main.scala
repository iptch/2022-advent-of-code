import scala.collection.mutable
import scala.io.Source
import scala.util.{Failure, Success, Using}

type Directory = mutable.HashMap[String, DirectoryItem]

enum DirectoryItem:
  case D(hashMap: Directory)
  case F(size: Int)

def newDir(): DirectoryItem = {
  DirectoryItem.D(mutable.HashMap[String, DirectoryItem]())
}

def computeSize(tree: Directory, sizes: mutable.ArrayBuffer[Int]): Int = {
  val itemSizes = for ((name, item) <- tree) yield {
    item match
      case DirectoryItem.D(hashMap) => computeSize(hashMap, sizes)
      case DirectoryItem.F(size) => size
  }
  val directorySize = itemSizes.sum
  sizes.append(directorySize)
  directorySize
}

@main
def main(): Unit = {
  val parseResult = Using(Source.fromFile("../input").bufferedReader()) { source =>
    // Parse!
    val root: Directory = mutable.HashMap[String, DirectoryItem]()
    val stack = mutable.Stack(root)
    var line: String = source.readLine()
    while (line != null) {
      val cwd: Directory = stack.top
      val parts = line.split(' ')
      parts.length match
        case 2 =>
          // $ ls
          while ({
            line = source.readLine()
            line != null && !line.startsWith("$")
          }) {
            val parts = line.split(' ')
            val newItem = parts(0).toIntOption match
              case Some(value) => DirectoryItem.F(value)
              case None => newDir()
            cwd.getOrElseUpdate(parts(1), newItem)
          }
        case 3 =>
          // $ cd ARG
          val arg = parts(2)
          if (arg == "..")
            stack.pop()
            if (stack.isEmpty)
              stack.push(root)
          else if (arg == "/")
            stack.clear()
            stack.push(root)
          else
            cwd.getOrElseUpdate(arg, newDir()) match
              case DirectoryItem.D(hashMap) => stack.push(hashMap)
              case DirectoryItem.F(size) => throw AssertionError("Cannot cd into file.")
          line = source.readLine()
    }
    root
  }
  val tree = parseResult match
    case Failure(exception) => throw exception
    case Success(value) => value

  val sizes = mutable.ArrayBuffer[Int]()
  val totalSize = computeSize(tree, sizes)

  val ans1 = sizes.filter(_ <= 100000).sum
  println(s"ans1 = ${ans1}")

  val freeSpace = 70000000 - totalSize
  val minToBeDeleted = 30000000 - freeSpace

  val ans2 = sizes.filter(_ >= minToBeDeleted).min
  println(s"ans2 = ${ans2}")
}