<script lang="ts">
// Contributors:
// * Contributor: <arvinra@student.chalmers.se>
// * Contributor: <rokanas@student.chalmers.se>
// * Contributor: <kaisa.arumeel@gmail.com>
// * Contributor: <alexandersafstrom@proton.me>

  import { onMount } from "svelte";
  import { API } from '../api';
  import type { AxiosError } from 'axios';
  import { slide } from "svelte/transition";
  import { getCSRFToken } from '../stores/csrfStore'; // Import CSRF token
  import { userRequests, type UserRequest } from '../stores/requestStore';

  interface User {
    id: string;
    name: string;
    is_admin: boolean;
  }
  type ErrorResponse = {
    err?: string;
  };

  let users: User[] = [];
  let errorMessage: string | null = null; // To store any error messages
  let showModal = false; // To toggle the modal visibility
  let userToDelete: string | null = null; // Store the username of the user to be deleted
  let expandedUser: string | null = null; // Store username of user panel currently expanded

  // Fetch users from the backend API
  const getUsers = async () => {
    try {
      const response = await API.get("/api/get-all-users/");
      console.log("API Response:", response.data);

      const data = response.data;
      users = data.users.map((user: { username: string, is_admin: boolean }) => ({
        id: user.username,
        name: user.username,
        is_admin: user.is_admin,
      }));
      console.log("Users fetched successfully:", users);
    } catch (err) {
      const axiosError = err as AxiosError<ErrorResponse>;
      errorMessage = axiosError.response?.data?.err || "An unknown error occurred.";
      console.error("Error getting users:", errorMessage);
    }
  };

  // Show the confirmation modal
  const confirmDelete = (username: string) => {
    userToDelete = username;
    errorMessage = null; // Reset any previous error messages
    showModal = true;
  };

  // Method to delete a user
  const deleteUser = async () => {
    if (!userToDelete) return;
    try {
      const response = await API.delete(`/api/delete-user/${userToDelete}/`, {
        headers: {
          'X-CSRFToken': getCSRFToken(),
        }
      });
      // Update the local state to remove the deleted user
      users = users.filter(user => user.id !== userToDelete);
      showModal = false; // Close modal after successful deletion
    } catch (err) {
      const axiosError = err as AxiosError<ErrorResponse>;
      errorMessage = axiosError.response?.data?.err || "An unknown error occurred.";
      console.error("Error deleting user:", errorMessage);
    }
  };

  function toggleExpandedUser (user: User): void {
    expandedUser = expandedUser === user.id ? null : user.id;
    }

  // Filter requests by user ID
  function getUserRequests(username: string): UserRequest[] {
    const allRequests = $userRequests; // Get all requests from the store
    return allRequests.filter((request) => request.user === username);
  }

  // Fetch users when the component is mounted
  onMount(() => {
    getUsers();
  });
</script>

{#if showModal}
  <div class="fixed inset-0 bg-gray-500 bg-opacity-75 flex justify-center items-center z-50">
    <div class="bg-white rounded-lg shadow-lg p-6 lg:w-1/3 w-2/3">
      <h3 class="text-lg text-tertiary font-bold">Confirm Deletion</h3>
      <p class="mt-2 text-sm text-tertiary">
        Are you sure you want to delete this user? This action cannot be undone.
      </p>
      {#if errorMessage}
        <p class="mt-2 text-sm text-red-500">
          {errorMessage}
        </p>
      {/if}
      <div class="mt-4 flex justify-end space-x-4">
        <button
          class="bg-gray-300 text-gray-700 px-4 py-2 rounded hover:bg-gray-400"
          on:click={() => {
            showModal = false;
            userToDelete = null;
            errorMessage = null; // Reset error message
          }}
        >
          Cancel
        </button>
        <button
          class="bg-red-500 text-white px-4 py-2 rounded hover:bg-red-600"
          on:click={deleteUser}
        >
          Delete
        </button>
      </div>
    </div>
  </div>
{/if}

<div class="h-fit bg-white rounded-lg shadow-md p-4 flex flex-col items-start">
  <h2 class="text-lg font-regular text-secondary">Manage Users</h2>
  <p class="text-sm text-tertiary mt-2">View and manage user accounts.</p>
  <ul class="mt-4 w-full space-y-2 max-h-96 overflow-y-auto">
    {#each users as user (user.id)}
      <li class="flex flex-col bg-gray-100 py-2 px-2 rounded-md">
        <div class="flex justify-between items-center w-full">
          <button
            type="button"
            class="flex items-center justify-between w-full py-2 px-3 rounded focus:outline-none 
            {expandedUser === user.id ? 'bg-gray-200' : 'bg-gray-100 hover:bg-gray-200'}"
            on:click={() => toggleExpandedUser(user)}
          >
            <!-- Left-side content -->
            <div class="flex items-center">
              <span class="text-tertiary">{user.name}</span>
            </div>
    
            <!-- Right-side content -->
            <div class="flex items-center space-x-2">
              {#if user.is_admin}
                <span class="text-secondary text-xs font-regular"><strong>ADMIN</strong></span>
              {/if}
              <span class="text-tertiary">{expandedUser === user.id ? '▲' : '▼'}</span>
            </div>
          </button>
          <button
            class="text-red-500 hover:text-red-700 focus:outline-none ml-4"
            aria-label="Delete user"
            on:click={() => confirmDelete(user.id)}
          >
            <svg
              xmlns="http://www.w3.org/2000/svg"
              class="h-5 w-5"
              viewBox="0 0 20 20"
              fill="currentColor"
            >
              <path
                fill-rule="evenodd"
                d="M6 2a1 1 0 00-1 1v1H3a1 1 0 100 2h1v9a2 2 0 002 2h8a2 2 0 002-2V6h1a1 1 0 100-2h-2V3a1 1 0 00-1-1H6zm3 3a1 1 0 011-1h2a1 1 0 011 1v1H9V5zm5 4a1 1 0 10-2 0v5a1 1 0 102 0V9zm-6 0a1 1 0 10-2 0v5a1 1 0 102 0V9z"
                clip-rule="evenodd"
              />
            </svg>
          </button>
        </div>

        <!-- Collapsible Panel -->
        {#if expandedUser === user.id}
          <div transition:slide class="mt-2 bg-gray-50 p-4 rounded-md">
            <p class="text-sm text-tertiary mb-2">
              <strong>Requests</strong>
            </p>
            {#if getUserRequests(user.name).length > 0}
              <ul>
                {#each getUserRequests(user.name) as request}
                  <li class="flex justify-between items-center py-1 border-b border-gray-300 last:border-none">
                    <span class="text-sm text-tertiary"><strong>ID:</strong> {request.request_id}</span>
                    <span class="text-sm text-tertiary"><strong>Date:</strong> {new Date(request.created_at * 1000).toLocaleDateString()}</span>
                  </li>
                {/each}
              </ul>
            {:else}
              <p class="text-sm text-gray-500 mt-2"><em>No requests available</em></p>
            {/if}
          </div>
        {/if}
      </li>
    {/each}
  </ul>
</div>
