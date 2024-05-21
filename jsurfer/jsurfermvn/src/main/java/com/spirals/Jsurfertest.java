import com.google.gson.JsonElement;
import com.google.gson.JsonParser;
import com.google.gson.stream.JsonReader;

import com.github.jsurfer.JSONSurfer;
import com.github.jsurfer.model.JsonPath;

import java.io.FileReader;
import java.io.IOException;

public class Jsurfertest {
    public static void main(String[] args) {
        try {
            JsonReader reader = new JsonReader(new FileReader("../../JsonFiles/ast.json"));
            JsonElement jsonElement = JsonParser.parseReader(reader);

            JSONSurfer surfer = JSONSurfer.gson(new GsonAdapter().getGson());

            JsonPath path = JsonPath.compile("$..author");

            surfer.surf(jsonElement, path, (matchingValue, valuePath) -> {
                System.out.println("Path: " + valuePath + ", Value: " + matchingValue);
            });

        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
