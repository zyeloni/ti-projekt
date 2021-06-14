package ranked.io.helpers;

import com.fasterxml.jackson.databind.ObjectMapper;
import com.fasterxml.jackson.databind.util.JSONPObject;
import org.apache.http.Header;
import org.apache.http.HttpHeaders;
import org.apache.http.HttpResponse;
import org.apache.http.NameValuePair;
import org.apache.http.client.HttpClient;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.DefaultHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicHeader;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;
import org.json.simple.JSONArray;
import org.json.simple.JSONObject;
import org.json.simple.parser.JSONParser;
import ranked.io.config.APIConfig;
import ranked.io.models.json.AuthModel;
import ranked.io.models.json.PlayerModel;

import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class PlayerHelper {

    public static String getPlayerIdFromUUID(String uuid) throws Exception {

        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpGet httpGet = new HttpGet(APIConfig.API_URL + "players/" + uuid);
        HttpResponse httpResponse = httpClient.execute(httpGet);

        return EntityUtils.toString(httpResponse.getEntity());
    }
}
