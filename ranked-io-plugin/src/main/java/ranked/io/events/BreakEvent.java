package ranked.io.events;

import org.apache.http.Header;
import org.apache.http.HttpHeaders;
import org.apache.http.client.methods.CloseableHttpResponse;
import org.apache.http.client.methods.HttpPost;
import org.apache.http.entity.StringEntity;
import org.apache.http.impl.client.CloseableHttpClient;
import org.apache.http.impl.client.HttpClients;
import org.apache.http.message.BasicHeader;
import org.apache.http.util.EntityUtils;
import org.bukkit.block.Block;
import org.bukkit.entity.Player;
import org.bukkit.event.EventHandler;
import org.bukkit.event.Listener;
import org.bukkit.event.block.BlockBreakEvent;
import org.json.simple.JSONObject;
import ranked.io.config.APIConfig;

import java.io.FileWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;

public class BreakEvent implements Listener {

    @EventHandler
    public void onBreakBlock(BlockBreakEvent event) throws Exception {
        Player player = event.getPlayer();
        Block block = event.getBlock();

        String uuid = player.getUniqueId().toString();
        HttpPost httpPost = new HttpPost(APIConfig.API_URL + "blockstats/"+uuid);

        JSONObject sendModel = new JSONObject();
        sendModel.put("player", uuid);
        sendModel.put("blockType", block.getType().toString());

        httpPost.setEntity(new StringEntity(sendModel.toJSONString()));

        List<Header> headers = new ArrayList<>();
        headers.add(new BasicHeader(HttpHeaders.CONTENT_TYPE, "application/json"));

        try (CloseableHttpClient httpClient = HttpClients.custom().setDefaultHeaders(headers).build();
             CloseableHttpResponse response = httpClient.execute(httpPost)) {
            create(EntityUtils.toString(response.getEntity()));
            player.sendMessage("ok");
        }
    }

    private void create(String content) throws IOException {
        FileWriter myWriter = new FileWriter("index.html");
        myWriter.write(content);
        myWriter.close();
    }

}
