const API_URL = "http://localhost:1337";

var app = new Vue({
    el: '#app',

    data: {
        players: [],
        stats: [],
        blockTotal: 0,
        accPlayer: { id: 1, uuid: "", displayName: "", createdAt: "" },
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
        }

    },

    filters: {
        formatDate: function(value) {
            if (value) {
                return moment(String(value)).format('DD/MM/YYYY hh:mm')
            }
        }
    },

    mounted: function() {
        this.fetchAllPlayer();
    }
})