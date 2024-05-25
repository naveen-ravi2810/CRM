<template>
    <div>
        <h2>This is Login page</h2>
        <form @submit.prevent="submitForm">
            <div>
                <label>Email</label>
                <input v-model="formData.email" name="email" required/>
            </div>
            <div>
                <label>Password</label>
                <input v-model="formData.password" type="password" name="password" required/>
            </div>
            <div>
                <input type="submit" value="Log in"/>
            </div>
        </form>
    </div>
</template>

<script>
export default {
    data() {
        return {
            formData: {
                email: '',
                password: '',
            }
        };
    },
    methods: {
        async submitForm() {
            try {
                const response = await fetch('http://localhost:8000/root_admin/login', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json'
                    },
                    body: JSON.stringify(this.formData)
                });

                if (response.ok) {
                    const data = await response.json()
                    localStorage.setItem("token", data.access_token)
                } else {
                    console.error('Failed to submit form data');
                }
            } catch (error) {
                console.error('An error occurred:', error);
            }
        }
    }
}
</script>

<style>

</style>
