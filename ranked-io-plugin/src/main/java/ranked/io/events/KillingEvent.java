package ranked.io.events;

import org.apache.http.Header;
import org.apache.http.HttpHeaders;
import org.apache.http.NameValuePair;
import org.apache.http.client.entity.UrlEncodedFormEntity;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicHeader;
import org.apache.http.message.BasicNameValuePair;
import org.apache.http.util.EntityUtils;
import org.bukkit.entity.Entity;
import org.bukkit.entity.LivingEntity;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.entity.EntityDeathEvent;
import org.json.simple.JSONObject;
import ranked.io.config.APIConfig;
import ranked.io.helpers.PlayerHelper;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class KillingEvent implements Listener {

    @EventHandler
    public void onMobDeath(EntityDeathEvent event) throws Exception {
        Entity target = event.getEntity();
        Player player = event.getEntity().getKiller();

        if (target instanceof Player || !(target instanceof LivingEntity) || !(player instanceof Player))
            return;

        String uuid = player.getUniqueId().toString();
        HttpPost httpPost = new HttpPost(APIConfig.API_URL + "entitystats/"+uuid);

        JSONObject sendModel = new JSONObject();
        sendModel.put("player", uuid);
        sendModel.put("entityType", target.getName());

        httpPost.setEntity(new StringEntity(sendModel.toJSONString()));

        List<Header> headers = new ArrayList<>();
        headers.add(new BasicHeader(HttpHeaders.CONTENT_TYPE, "application/json"));

        try (CloseableHttpClient httpClient = HttpClients.custom().setDefaultHeaders(headers).build();
             CloseableHttpResponse response = httpClient.execute(httpPost)) {
        }
    }
}
