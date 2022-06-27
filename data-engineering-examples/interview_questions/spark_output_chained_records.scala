// Sample Input:
// id,pid
// a,b
// b,c
// d,e
// f,g
// g,h
// i,j

// Sample Output:
// id,pid
// a,b
// b,c
// f,g
// g,h

import org.apache.spark.sql.functions.{col, array, struct, explode}

val df = spark
            .sparkContext
            .parallelize(Seq(
                ("a","b"),
                ("b","c"),
                ("d","e"),
                ("f","g"),
                ("g","h"),
                ("i","j")))
            .toDF("id","pid")

val result = df.as("df1")
               .join(df.as("df2"), col("df1.pid") === col("df2.id"))
               .withColumn(
                 "arr_of_structs", 
                 array(
                   struct(col("df1.id"), col("df1.pid")), 
                   struct(col("df2.id"), col("df2.pid"))))
               .withColumn("exploded_array", explode(col("arr_of_structs")))
               .select(col("exploded_array.id"), col("exploded_array.pid"))

result.show(false)
