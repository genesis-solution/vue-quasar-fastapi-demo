<template>
    <q-page>
      <q-card class="q-pa-md">
        <q-card-section class="text-center">
          <h2 class="text-h4">Register</h2>
          <q-form @submit.prevent="register" class="form-signin">
            <q-input
              outlined
              v-model="first_name"
              label="First name"
              type="text"
              class="input-signin"
              required
            />
            <q-input
              outlined
              v-model="last_name"
              label="Last name"
              type="text"
              class="input-signin"
              required
            />
            <q-input
              outlined
              v-model="email"
              label="Email"
              type="email"
              class="input-signin"
              required
            />
            <q-input
              outlined
              v-model="password"
              label="Password"
              type="password"
              class="input-signin"
              required
            />
            <q-input
              outlined
              v-model="confirm_password"
              label="Confirm Password"
              type="password"
              class="input-signin"
              required
            />
            <q-btn type="submit" color="primary" label="Sign up" class="button-signin" />
          </q-form>
          <router-link to="/signin">To Signin</router-link>
        </q-card-section>
      </q-card>
    </q-page>
  </template>

<style>
.text-center {
    text-align: center;
}
.form-signin {
    margin: auto;
    text-align: center;
}
.input-signin {
  width: 250px;
  margin: auto;
  margin-bottom: 20px;
}
.button-signin {
    width: 250px;
    margin-bottom: 10px;
}
</style>
  
  <script>
  import axios from 'axios';
  export default {
    data() {
      return {
        first_name: '',
        last_name: '',
        email: '',
        password: '',
        confirm_password: '',
      };
    },
    methods: {
      register() {
        if (this.password == "" || this.first_name == "" || this.last_name == "" || this.email == "") {
          alert("Please fill out this fields.")
          return
        }
        if (this.password != this.confirm_password) {
          alert("Please confirm your password.")
        }
        else {
          axios.post('http://localhost:8000/signup', {
            first_name: this.first_name,
            last_name: this.last_name,
            email: this.email,
            password: this.password
          })
          .then((response) => {
              if (response.data.status == 200)
              {
                this.$router.push('/signin')
              }
          })
          .catch((error) => {
              console.log(error);
          });
        }
        // handle sign in logic here
      },
    },
  };
  </script>