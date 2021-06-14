package ranked.io.events;

import org.apache.http.Header;
import org.apache.http.HttpHeaders;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicHeader;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.player.PlayerJoinEvent;
import org.json.simple.JSONObject;
import ranked.io.config.APIConfig;
import java.util.ArrayList;
import java.util.List;

public class JoinEvent implements Listener {

    @EventHandler
    public void onPlayerEvent(PlayerJoinEvent event) throws Exception {
        Player player = event.getPlayer();
        HttpPost httpPost = new HttpPost(APIConfig.API_URL + "players/");

        String uuid = player.getUniqueId().toString();
        String displayName = player.getDisplayName();

        JSONObject sendModel = new JSONObject();
        sendModel.put("uuid", uuid);
        sendModel.put("displayName", displayName);

        httpPost.setEntity(new StringEntity(sendModel.toJSONString()));

        List<Header> headers = new ArrayList<>();
        headers.add(new BasicHeader(HttpHeaders.CONTENT_TYPE, "application/json"));

        try (CloseableHttpClient httpClient = HttpClients.custom().setDefaultHeaders(headers).build();
             CloseableHttpResponse response = httpClient.execute(httpPost)) {
        }
    }

}
