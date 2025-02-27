# Use Node.js image
FROM node:22

# Set the working directory
WORKDIR /app

# Copy package.json and install dependencies
COPY package*.json ./
RUN npm install

# Copy all files
COPY . .

# Expose React port
EXPOSE 3000

# Start React app
CMD ["npm", "start"]
