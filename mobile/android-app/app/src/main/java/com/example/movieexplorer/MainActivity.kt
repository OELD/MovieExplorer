package com.example.movieexplorer

import android.os.Bundle
import androidx.appcompat.app.AppCompatActivity
import android.widget.*
import okhttp3.*
import org.json.JSONArray
import java.io.IOException

class MainActivity : AppCompatActivity() {
    private val client = OkHttpClient()
    override fun onCreate(savedInstanceState: Bundle?) {
        super.onCreate(savedInstanceState)
        val layout = LinearLayout(this).apply {
            orientation = LinearLayout.VERTICAL
            setPadding(16,16,16,16)
        }
        val listView = ListView(this)
        layout.addView(listView)
        setContentView(layout)

        fetchMovies { movies ->
            runOnUiThread {
                val titles = movies.map { "${it["title"]} (${it["year"]})" }
                listView.adapter = ArrayAdapter(this, android.R.layout.simple_list_item_1, titles)
            }
        }
    }

    private fun fetchMovies(callback: (List<Map<String, Any>>) -> Unit) {
        val request = Request.Builder()
            .url("http://10.0.2.2:8000/movies")
            .build()
        client.newCall(request).enqueue(object: Callback {
            override fun onFailure(call: Call, e: IOException) { e.printStackTrace() }
            override fun onResponse(call: Call, response: Response) {
                response.body?.string()?.let {
                    val json = JSONArray(it)
                    val list = mutableListOf<Map<String, Any>>()
                    for (i in 0 until json.length()) {
                        val obj = json.getJSONObject(i)
                        list.add(mapOf(
                            "title" to obj.getString("title"),
                            "year" to obj.getInt("year")
                        ))
                    }
                    callback(list)
                }
            }
        })
    }
}
