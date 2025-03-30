<template>
  <div class="home-container">
    <h1> Wilcome to Quiz Master </h1>
     <h2> Designed by Pallavi Sinha</h2>
     <h3> IIT Madras B.S Degree Programme</h3>
     <div class="button-group">
           <router-link to ="/login" class="btn">
                 <button> Login</button> 
           </router-link>
           <router-link to ="/Register" class="btn">
                <button> Register</button> 
           </router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: 'HomePage',
 
};
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
/* Full-screen centered layout */
.home-container {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background: linear-gradient(135deg, #801eb6, #00c6ff);
  color: rgb(192, 180, 75);
  font-family: 'Arial', sans-serif;
  text-align: center;
  padding: 20px;
}

/* Main heading */
.home-container h1 {
  font-size: 36px;
  font-weight: bold;
  margin-bottom: 10px;
}

/* Subheading */
.home-container h2 {
  font-size: 20px;
  font-weight: 400;
  margin-bottom: 5px;
}

/* College Name */
.home-container h3 {
  font-size: 18px;
  font-weight: 300;
  margin-bottom: 30px;
}

/* Button container */
.button-group {
  display: flex;
  gap: 20px;
}

/* Buttons */
.btn {
  background: white;
  color: #007bff;
  padding: 12px 24px;
  border: none;
  border-radius: 8px;
  cursor: pointer;
  text-decoration: none;
  font-size: 18px;
  font-weight: bold;
  transition: 0.3s;
}

.btn:hover {
  background: #0056b3;
  color: white;
  transform: scale(1.05);
}

</style>
