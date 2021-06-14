package ranked.io.models.json;

import java.util.Date;

class Role{
    public int id;
    public String name;
    public String description;
    public String type;
}

class User{
    public int id;
    public String username;
    public String email;
    public String provider;
    public boolean confirmed;
    public boolean blocked;
    public Role role;
    public Date created_at;
    public Date updated_at;
}

public class AuthModel {
    public String jwt;
    public User user;
}