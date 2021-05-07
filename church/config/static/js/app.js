const app = Vue.createApp({
    delimiters: ["[[", "]]"],
    data() {
        return {
            firstName: '',
            middleName: '',
            lastName: '',
            covidID: '',
            currentID: '',
            message: '',
            csrftoken: '',
        }
    },
    methods: {
        async verifyCovidReference() {
            await axios.get('http://127.0.0.1:8000/user/api/' + this.covidID)
            .then((res) => {
                console.log(res)
                if (this.firstName == res.data.first_name && this.middle_name == res.data.middleName && this.lastName == res.data.last_name) {
                  this.updateVerify()
                } else {
                  this.message = 'Verification failed. The names are not equal or the wrong covid ID reference number was given.'
                }
            })
            .catch((error) => {
                console.log(error)
                this.message = 'The Covid API could not be accessed.'
            })
        },
        async updateVerify() {
          axios.put('http://127.0.0.1:8001/ref/api/' + this.currentID, {
            user: this.currentID,
            covid_reference_id: this.covidID,
            verified: true
          }, {
            headers: {
              'X-CSRFTOKEN': this.csrftoken
            },
          }).then((res) => {
            console.log(res)
            this.message = 'Verification success! Refresh to see updated results'
          }).catch((error) => {
            console.log(error)
            // this.message = 'Name is correct, but there is an error in updating verification status.'
          })
        }
    },
    mounted() {
        this.firstName = firstName;
        this.middleName = middleName;
        this.lastName = lastName;
        this.covidID = covidID;
        this.currentID = currentID;
        this.csrftoken = csrftoken;
    }
})

app.mount('#app')
