To create a Backstage app, you don't need to go to the Spotify Developer website. Instead, you can use the Backstage CLI to scaffold a new Backstage application. Here's how you can do it:

1. **Install Node.js**: Ensure you have Node.js installed on your system (preferably version 16 or later).

2. **Install Backstage CLI**: Run the following command to globally install the Backstage CLI:
    ```bash
    npm install -g @backstage/create-app
    ```

3. **Create a Backstage App**: Use the CLI to create a new Backstage app by running:
    ```bash
    npx @backstage/create-app
    ```
    Follow the prompts to name your app and set it up.

4. **Navigate to the App Directory**: Once the app is created, navigate to the directory:
    ```bash
    cd <your-app-name>
    ```

5. **Run the App Locally**: Start the development server to verify the app works:
    ```bash
    yarn dev
    ```

Once your Backstage app is created, you can use your Dockerfile to containerize it.

FROM node:16-bullseye-slim

# Install necessary dependencies
RUN apt-get update && \
    apt-get install -y --no-install-recommends python3 build-essential git ca-certificates && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Set working directory
WORKDIR /app

# Copy repo content
COPY . .

# Install dependencies
RUN yarn install --frozen-lockfile

# Build the app
RUN yarn build

# Expose port 7007
EXPOSE 7007

# Start the app
CMD ["yarn", "start"]