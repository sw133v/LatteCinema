<template>
  <div>
    <!-- <h1>Signup</h1> -->

    <account-error-list v-if="authError"></account-error-list>

    <!-- <form @submit.prevent="signup(credentials)">
      <div>
        <label for="username">Username: </label>
        <input  v-model="credentials.username" type="text" id="username" required/>
      </div>
      <div>
        <label for="password1">Password: </label>
        <input v-model="credentials.password1" type="password" id="password1" required />
      </div>
      <div>
        <label for="password2">Password Confirmation:</label>
        <input v-model="credentials.password2" type="password" id="password2" required />
      </div>
      <div>
        <button>Signup</button>
      </div>
    </form> -->
    <div class="page-content">
      <div class="form-v5-content">
        <form class="form-detail" @submit.prevent="signup(credentials)">
          <h2>Signup</h2>
          <div class="form-row">
            <label for="username">Username</label>
            <input type="text" v-model="credentials.username" name="full-name" id="username" class="input-text" placeholder="User Name" required>
            <!-- <i class="fas fa-user"></i> -->
          </div>
          <div class="form-row">
            <label for="password1">Password</label>
            <input type="password" v-model="credentials.password1" name="your-email" id="password1" class="input-text" placeholder="Password" required>
            <!-- <i class="fas fa-envelope"></i> -->
          </div>
          <div class="form-row">
            <label for="password2">Password Confirmation</label>
            <input type="password" v-model="credentials.password2" name="password" id="password2" class="input-text" placeholder="Password Confirmation" required>
            <!-- <i class="fas fa-lock"></i> -->
          </div>
          <div class="form-row-last">
            <input type="submit" name="register" class="register" value="회원 가입">
          </div>
        </form>
        <div class="text-center p-t-115">
          <span class="txt1">
            You already have account
          </span>

          <router-link :to="{ name: 'login' }">Login</router-link>
        </div>
        <br>
      </div>
    </div>
  </div>
</template>

<script>
  import { mapActions, mapGetters } from 'vuex'
  import AccountErrorList from '@/components/AccountErrorList.vue'

  export default {
    name: 'SignupView',
    components: {
      AccountErrorList,
    },
    data() {
      return {
        credentials: {
          username: '',
          password1: '',
          password2: '',
        }
      }
    },
    computed: {
      ...mapGetters(['authError'])
    },
    methods: {
      ...mapActions(['signup'])
    },
  }
</script>

<style>
.page-content {
  width: 100%;
  margin:  0 auto;
  background: #f2f2f2;
  display: flex;
  display: -webkit-flex;
  justify-content: center;
  -o-justify-content: center;
  -ms-justify-content: center;
  -moz-justify-content: center;
  -webkit-justify-content: center;
  align-items: center;
  -o-align-items: center;
  -ms-align-items: center;
  -moz-align-items: center;
  -webkit-align-items: center;
}
.form-v5-content  {
  background: #fff;
  width: 670px;
  border-radius: 8px;
  -o-border-radius: 8px;
  -ms-border-radius: 8px;
  -moz-border-radius: 8px;
  -webkit-border-radius: 8px;
  margin: 175px 0;
  font-family: 'Roboto', sans-serif;
  color: #333;
  font-weight: 400;
  position: relative;
  font-size: 18px;
}
.form-v5-content .form-detail {
  padding: 30px 45px 30px 45px;
  position: relative;
}
.form-detail h2 {
  font-weight: 700;
  font-size: 25px;
  text-align: center;
  position: relative;
  padding: 3px 0 20px;
  margin-bottom: 40px;
}
.form-detail h2::after {
  background: #3786bd;
  width: 50px;
  height: 2px;
  content: "";
  position: absolute;
  top: 100%;
  left: 50%;
    transform: translateX(-50%);
    -o-transform: translateX(-50%);
  -ms-transform: translateX(-50%);
  -moz-transform: translateX(-50%);
  -webkit-transform: translateX(-50%);
}
.form-detail .form-row {
  position: relative;
}
.form-detail .form-row-last {
  text-align: center;
}
.form-detail label {
  display: block;
  font-size: 18px;
  padding-bottom: 10px;
}
.form-detail .input-text {
  margin-bottom: 26px;
}
.form-detail input {
  width: 94.5%;
    padding: 10.5px 15px;
    border: 1px solid #e5e5e5;
    appearance: unset;
    -moz-appearance: unset;
    -webkit-appearance: unset;
    -o-appearance: unset;
    -ms-appearance: unset;
    outline: none;
    -moz-outline: none;
    -webkit-outline: none;
    -o-outline: none;
    -ms-outline: none;
    border-radius: 4px;
  -o-border-radius: 4px;
  -ms-border-radius: 4px;
  -moz-border-radius: 4px;
  -webkit-border-radius: 4px;
  font-family: 'Roboto', sans-serif;
  font-weight: 400;
  font-size: 18px;
}
.form-detail input:focus {
  border: 1px solid #b3b3b3;
}
.form-detail .register {
  font-size: 18px;
  color: #fff;
  background: #3786bd;
  border-radius: 5px;
  -o-border-radius: 5px;
  -ms-border-radius: 5px;
  -moz-border-radius: 5px;
  -webkit-border-radius: 5px;
  width: 180px;
  box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.2);
  -o-box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.2);
  -ms-box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.2);
  -moz-box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.2);
  -webkit-box-shadow: 0px 5px 15px 0px rgba(0, 0, 0, 0.2);
  border: none;
  margin: 19px 0 40px;
  cursor: pointer;
}
.form-detail .register:hover {
  background: #2f73a3;
}
.form-detail .form-row-last input {
  padding: 14px;
}
.form-detail i {
  font-size: 14px;
  color: #999;
  right: 15px;
  top: 50%;
  transform: translateX(-50%);
  position: absolute;
}
input::-webkit-input-placeholder { /* Chrome/Opera/Safari */
  color: #999;
  font-size: 16px;
}
input::-moz-placeholder { /* Firefox 19+ */
  color: #999;
  font-size: 16px;
}
input:-ms-input-placeholder { /* IE 10+ */
  color: #999;
  font-size: 16px;
}
input:-moz-placeholder { /* Firefox 18- */
  color: #999;
  font-size: 16px;
}

/* Responsive */
@media screen and (max-width: 767px) {
  .form-v5-content {
      margin: 175px 20px;
  }
}
.txt1 {
  font-family: Poppins-Regular;
  font-size: 13px;
  color: #666666;
  line-height: 1.5;
}

</style>
