const API_URL = "http://109.125.210.252:1337";
const MC_HOST = "109.125.210.252:25565";
const API_PLUGIN = "http://109.125.210.252:4567/v1"

var app = new Vue({
    el: '#app',

    data: {
        players: [],
        killStats: [],
        deathsStat: [],
        stats: [],
        blockTotal: 0,
        accPlayer: { id: 1, uuid: "", displayName: "", createdAt: "" },
        lastKills: [],
        allStats: [],
        allKills: [],
        loggedPlayers: [],
        serverStatus: 'unchecked',
    },

    methods: {

        fetchAllPlayer: function() {
            let vm = this;
            axios.get(`${API_URL}/players/`)
                .then(function(response) {
                    vm.players = JSON.parse(JSON.stringify(response.data));
                })
                .catch(function(error) {
                    console.log(error);
                })
        },

        fetchStats: function(uuid) {
            vm = this;
            axios.get(`${API_URL}/entitystats/${uuid}`)
                .then(function(response) {
                    vm.stats = JSON.parse(JSON.stringify(response.data));
                    $('#statsModal').modal('show');
                    vm.accPlayer = vm.findPlayerById(uuid);
                })
                .catch(function(error) {
                    vm.stats = [];
                });

            axios.get(`${API_URL}/blockstats/${uuid}`)
                .then(function(response) {
                    vm.blockTotal = response.data[0].total;
                })
                .catch(function(error) {
                    vm.blockTotal = 0;
                });

            axios.get(`${API_URL}/kills/killer/${uuid}`)
                .then(function(response) {
                    vm.killStats = JSON.parse(JSON.stringify(response.data));
                })
                .catch(function(error) {
                    vm.killStats = [];
                });

            axios.get(`${API_URL}/kills/victim/${uuid}`)
                .then(function(response) {
                    vm.deathsStat = JSON.parse(JSON.stringify(response.data));
                })
                .catch(function(error) {
                    vm.killStats = [];
                });
        },


        findPlayerById: function(id) {
            let vm = this;

            for (i = 0; i < vm.players.length; i++) {
                if (vm.players[i].id == id)
                    return vm.players[i];
            }

            return null;
        },

        findPlayerByUUID: function(id) {
            let vm = this;

            for (i = 0; i < vm.players.length; i++) {
                if (vm.players[i].uuid == id)
                    return vm.players[i];
            }

            return null;
        },

        getTotalEntityStats: function() {
            let vm = this;
            var count = 0;
            for (i = 0; i < vm.stats.length; i++) {
                count += vm.stats[i].total;
            }
            return count;
        },

        fetchLastKill: function() {
            let vm = this;

            axios.get(`${API_URL}/lastkills/`)
                .then(function(response) {
                    vm.lastKills = JSON.parse(JSON.stringify(response.data));
                })

        },

        fetchAllStats: function() {
            let vm = this;
            axios.get(`${API_URL}/stats/`)
                .then(function(response) {
                    vm.allStats = JSON.parse(JSON.stringify(response.data));
                })
        },

        getStatsTotal: function(id) {
            let vm = this;
            for (i = 0; i < vm.allStats.length; i++)
                if (vm.allStats[i].player == id)
                    return vm.allStats[i].total


            return 0;
        },

        fetchAllKills: function() {
            let vm = this;
            axios.get(`${API_URL}/kills/`)
                .then(function(response) {
                    vm.allKills = JSON.parse(JSON.stringify(response.data));
                });
        },

        getKills: function(id) {
            let kills = 0;
            let vm = this;
            for (i = 0; i < vm.allKills.length; i++)
                if (vm.allKills[i].killer == id)
                    kills++;

            return kills;
        },

        getDeaths: function(id) {
            let deaths = 0;
            let vm = this;
            for (i = 0; i < vm.allKills.length; i++)
                if (vm.allKills[i].victim == id)
                    deaths++;

            return deaths;
        },

        fetchLoggedPlayers: function() {
            let vm = this;
            axios.get(`${API_PLUGIN}/players`)
                .then(function(response) {
                    vm.loggedPlayers = JSON.parse(JSON.stringify(response.data));
                    vm.serverStatus = 'on';
                }).catch(function(params) {
                    vm.serverStatus = 'off';
                });
        },


        fetch: function() {
            let vm = this;

            setInterval(function() {
                vm.fetchLastKill();
                vm.fetchAllStats();
                vm.fetchAllKills();
                vm.fetchLoggedPlayers();
            }, 5000);
        },

        isOnline: function(uuid) {
            let vm = this;

            for (i = 0; i < vm.loggedPlayers.length; i++)
                if (vm.loggedPlayers[i].uuid == uuid)
                    return true;

            return false;
        },

        getIdFromUuid: function(uuid) {
            let vm = this;

            for (i = 0; i < vm.players.length; i++) {
                let x = vm.players[i];

                if (x.uuid == uuid)
                    return x.id;
            }
        }

    },


    filters: {
        formatDate: function(value) {
            if (value) {
                return moment(String(value)).format('DD/MM/YYYY HH:mm')
            }
        }
    },

    mounted: function() {
        let vm = this;
        this.fetch();
        this.fetchAllPlayer();
        this.fetchLastKill();
        this.fetchAllStats();
        this.fetchAllKills();
        this.fetchLoggedPlayers();

        setTimeout(function() {
            tippy('[data-tippy-content]', {
                allowHTML: true,
                arrow: true,
            });

            $('#mainTable').DataTable({
                language: {
                    url: '//cdn.datatables.net/plug-ins/1.10.25/i18n/Polish.json'
                }
            });
        }, 1000);

        setTimeout(function() {
            $('.loading').addClass('d-none');
            $('#app').removeClass('d-none');

            animateCSS('#app', 'backInDown');
        }, 1200);
    }
})