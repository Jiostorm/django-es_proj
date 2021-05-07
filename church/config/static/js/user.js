const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data() {
        return {
            // Base Information
            refID: '',
            firstName: '',
            // Processed Information
            covidID: '',
            code: '',
            date_quarantine_ends: '',
        }
    },
    methods: {
        async getVerified() {
            await axios.get('http://127.0.0.1:8001/ref/api/' + this.refID)
            .then((res) => {
                console.log(res)
                if (res.data.verified == true) {
                    this.covidID = res.data.covid_reference_id
                    this.getCovidStatus()
                } else {
                    this.code = 'The user\'s Covid Reference ID is still not yet verified.'
                }
            })
            .catch((error) => {
                console.log(error)
                this.code = 'The user\'s Covid Reference ID is still not yet verified.'
            })
        },
        async getCovidStatus() {
          axios.get('http://127.0.0.1:8000/user/api/' + this.covidID)
          .then((res) => {
                console.log(res)
                if(res.data.code != null) {
                    this.code = 'Code: ' + res.data.code
                    if(res.data.quarantine_ends != null) {
                        const month = ["January", "February", "March", "April", "May", "June",
                        "July", "August", "September", "October", "November", "December"];
                        date = new Date(res.data.quarantine_ends)
                        this.date_quarantine_ends = `Date Quarantine Ends: ${month[date.getMonth()]} ${date.getDate()}, ${date.getFullYear()}`
                    }
                } else {
                    this.code = `${this.firstName} has no record on Covid.`
                }
          }).catch((error) => {
                console.log(error)
          })
        }
    },
    mounted() {
        this.refID = refID;
        this.firstName = firstName;
        this.getVerified();
    }
})

app.mount('#covid_ref')
