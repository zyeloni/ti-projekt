package ranked.io.helpers;

import org.apache.http.HttpResponse;
import org.apache.http.client.methods.HttpGet;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.util.EntityUtils;
import ranked.io.config.APIConfig;

public class PlayerHelper {

    public static String getPlayerIdFromUUID(String uuid) throws Exception {

        CloseableHttpClient httpClient = HttpClients.createDefault();
        HttpGet httpGet = new HttpGet(APIConfig.API_URL + "players/" + uuid);
        HttpResponse httpResponse = httpClient.execute(httpGet);

        return EntityUtils.toString(httpResponse.getEntity());
    }
}
