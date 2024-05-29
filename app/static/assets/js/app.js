const { createApp } = Vue;

        createApp({
            data() {
                return {
                    user: null
                };
            },
            methods: {
                handleCredentialResponse(response) {
                    const data = jwt_decode(response.credential);
                    this.user = {
                        name: data.name,
                        email: data.email,
                        picture: data.picture
                    };
                    // Store the JWT token in localStorage
                    localStorage.setItem('google_jwt', response.credential);
                },
                logout() {
                    this.user = null;
                    // Remove the JWT token from localStorage
                    localStorage.removeItem('google_jwt');
                }
            },
            mounted() {
                window.handleCredentialResponse = this.handleCredentialResponse;
            }
        }).mount('#app');