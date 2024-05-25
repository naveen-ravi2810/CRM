<template lang="">
    <div>
        <table class="tb-profile">
            <tr class="tb-row" v-for="value, key in profile">
                <td>{{ key }}</td>
                <td>{{ value }}</td>
            </tr>
        </table>
        this is profile p[age]
    </div>
</template>
<script>
    export default {
        name:'Profile',
        data() {
            return {
                profile : null
            }
        },
        async created() {
            const resp = await fetch("http://localhost:8000/root_admin/profile", {
                headers : {
                    'Authorization': `Bearer ${localStorage.getItem('token')}`
                }
            })
            if (resp.ok) {
                this.profile = await resp.json()
                
            }
        },
    }
</script>
<style>
    .tb-profile {
    width: 100%;
    border-collapse: collapse;
    margin: 20px 0;
    font-size: 18px;
    text-align: left;
}

.tb-profile, .tb-profile th, .tb-profile td {
    border: 1px solid #ddd;
}

.tb-profile th, .tb-profile td {
    padding: 12px 15px;
}

.tb-profile tr {
    border-bottom: 1px solid #ddd;
}

.tb-profile tr:nth-of-type(even) {
    background-color: #f3f3f3;
}


.tb-cell.key {
    font-weight: bold;
    background-color: #4CAF50;
    color: white;
}

.tb-cell.value {
    color: #555;
}

p {
    margin-top: 20px;
    font-size: 16px;
    color: #333;
}
</style>