package ranked.io;

import org.bukkit.Bukkit;
import org.bukkit.plugin.java.JavaPlugin;
import ranked.io.events.KillingEvent;
import ranked.io.events.JoinEvent;

import java.util.logging.Logger;

public final class Rankedio extends JavaPlugin {

    Logger logger = Bukkit.getLogger();

    @Override
    public void onEnable() {
        Bukkit.getServer().getPluginManager().registerEvents(new KillingEvent(),this);
        Bukkit.getServer().getPluginManager().registerEvents(new JoinEvent(), this);
    }

    @Override
    public void onDisable() {

    }
}
